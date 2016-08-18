#!/usr/bin/python

"""
(C) Copyright 2012 Altair Engineering, Inc.  All rights reserved.
This code is provided "as is" without any warranty, express or implied, or
indemnification of any kind.  All other terms and conditions are as
specified in the Altair PBS EULA.

Assumption:
 - Administrator has already updated the PBS Server and Scheduler with the
   new Intel Xeon Phi custom resources, AND restarted the daemons.
    + $PBS_HOME/server_priv/resourcedef
    + $PBS_HOME/sched_priv/sched_config
 - If number of devices change within the host, the administrator will need
   to delete existing vnode and natural node definitions from PBS before the
   new configuration will take effect.
   + $PBS_EXEC/bin/qmgr -c "d n hostname-mic#'
   + $PBS_EXEC/bin/qmgr -c "d n hostname"
   + $PBS_EXEC/sbin/pbs_mom -s remove mic_vnodedef

Purpose:
Automatically interrogate the Intel Xeon Phi command micinfo for useful
attributes to consider in scheduling jobs to the device(s). This script
will be executed automatically at initial start of PBS MOM on the host,
and write a mic_vnodedef configuration file to a PBS MOM directory.
"""

import sys
import os
import subprocess
import re
from socket import gethostname

# Set to 1 for debug messages
DEBUGON = 0

"""
Source PBS_CONF_FILE into environment AND construct common PBS commands
Source in the /etc/pbs.conf; it is 'good practice' to incorporate this so that
you are referring to the correct PBS Professional commands. Reduces some
hard coding, too.
"""

# Define PBS_CONF_FILE variable
if (sys.platform == 'win32'):
    os.environ['PBS_CONF_FILE'] = 'C:\Program Files\PBS Pro\pbs.conf'
else:
    os.environ['PBS_CONF_FILE'] = '/etc/pbs.conf'

if os.path.isfile(os.environ['PBS_CONF_FILE']):
    pbs_conf = open(os.environ['PBS_CONF_FILE'], 'r')
    for line in pbs_conf:
        os.environ[line.split("=")[0]] = line.split("=")[1].strip('\n')
    pbs_conf.close()
else:
    print "Unable to find PBS_CONF_FILE ... " + os.environ['PBS_CONF_FILE']
    sys.exit(1)

# Construct some common PBS Commands. Client Commands are assumed to be
# on the execution nodes. Some examples:
# pbsnodes = os.environ['PBS_EXEC'] + '/bin/pbsnodes'
# qmgr = os.environ['PBS_EXEC'] + '/bin/qmgr'
# pbs_mom = os.environ['PBS_EXEC'] + '/sbin/pbs_mom'

# Intel Xeon Phi Definitions
INTEL_MIC = '/opt/intel/mic'
if DEBUGON:
    print 'INTEL_MIC = ' + INTEL_MIC

if os.path.isfile(INTEL_MIC + '/bin/micinfo'):
    INTEL_MICINFO = INTEL_MIC + '/bin/micinfo'
else:
    INTEL_MICINFO = '/usr/bin/micinfo'

if DEBUGON:
    print 'INTEL_MICINFO = ' + INTEL_MICINFO

# Determine short hostname of system. This will be used to construct the
# mic_vnodedef.cfg file that defines the Intel Xeon Phi device(s) within
# PBS Professional.
hostname = gethostname().split(".", 1)[0]
if DEBUGON:
    print "Host short name: " + hostname

# Determine total number of cpus on the system. This will be used in the construction
# of the mic_vnodedef.cfg file that defines the Intel Xeon Phi device(s) within
# PBS Professional
if 'SC_NPROCESSORS_ONLN' in os.sysconf_names:
    ncpus = os.sysconf("SC_NPROCESSORS_ONLN")
    if isinstance(ncpus, int) and ncpus > 0:
        if DEBUGON:
            print "Host Total CPUs: " + str(ncpus)

# Determine total physical memory on the system. This will be used in the construction
# of the mic_vnodedef.cfg file that defines the Intel Xeon Phi device(s) within
# PBS Professional
cmd_meminfo = subprocess.Popen('cat /proc/meminfo', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in cmd_meminfo.stdout:
    if re.search(r"MemTotal", line):
        memory = re.match(r"MemTotal:\s+(.*)", line).group(1).replace(" ", "").lower()
        if DEBUGON:
            print "Host Total Memory: " + memory

"""
After defining the environment, we are now ready to start interrogating the Intel Xeon Phi
for attributes that will be useful for scheduling jobs (e.g., placement, allocation, etc).
BIG ASSUMPTION: Administrator has already updated $PBS_HOME/server_priv/resourcedef file
with the new Intel Xeon Phi custom resources, AND restarted the PBS Server.
"""
mic_global_attribute = {}
current_mic = {}

if os.path.isdir(INTEL_MIC):
    print "Intel Xeon Phi package installed... Preparing to execute."
    if os.path.isfile(INTEL_MICINFO):
        print "Found " + INTEL_MICINFO
        print "Detecting Intel Xeon Phi Device(s)..."

        # Construct the Intel Xeon Phi micinfo command line as cmd, so we can parse
        # the output for valuable data.
        cmd_micinfo = INTEL_MICINFO
        cmd_micinfo = subprocess.Popen(cmd_micinfo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # We will iterate through STDOUT cherry picking the information we need to
        # construct mic_vnodedef.cfg file
        for line in cmd_micinfo.stdout:
            # Detecting Intel Xeon Phi Driver Version, and pushing to the
            # the "global" mic attribute dictionary.
            # Usage: MIC driver version, host-based, meta-data, grouping
            if re.search(r"Driver Version", line):
                mic_driver = re.match(r"\s+Driver Version\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC Driver Version: " + mic_driver
                mic_global_attribute['mic_driver'] = mic_driver

            # Detecting Intel Xeon Phi MPSS Version, and pushing to the
            # the "global" mic attribute dictionary.
            # Usage: MIC MPSS version, host-based, meta-data, grouping
            if re.search(r"MPSS Version", line):
                mic_mpss = re.match(r"\s+MPSS Version\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC MPSS Version: " + mic_mpss
                mic_global_attribute['mic_mpss'] = mic_mpss

            # Detecting Intel Xeon Phi Device ID and Device Name. Introducing the
            # "current" mic attribute dictionary so that we can associate
            # attributes of the device to the correct Device ID
            # Usage: MIC device ID, vnode-based, requestable (benchmarking?), placement
            #        MIC name, vnode-based, meta-data
            if re.search(r"^Device", line):
                current_mic_attribute = {}
                if DEBUGON:
                    print "Found Device " + line[:-1]
                (mic_id, mic_name) = re.match(r"Device No: (\d+),\s+Device Name: (\w+)", line).group(1, 2)
                if DEBUGON:
                    print "Current MIC ID: " + mic_id
                if DEBUGON:
                    print "Current MIC Name: " + mic_name
                current_mic_attribute['mic_id'] = mic_id
                current_mic_attribute['mic_name'] = mic_name
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi Flash Version, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC flash version, vnode-based (Does all MIC in a system require same version?), meta-data
            if re.search(r"Flash Version", line):
                mic_flash = re.match(r"\s+Flash Version\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC Flash Version: " + mic_flash
                current_mic_attribute['mic_flash'] = mic_flash
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi uOS Version, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC micro-OS version, vnode-based, meta-data
            if re.search(r"UOS Version", line):
                mic_uos = re.match(r"\s+UOS Version\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC UOS Version: " + mic_uos
                current_mic_attribute['mic_uos'] = mic_uos
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi Total Number of Active Cores, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC number of cores on the device, vnode-based, requestable, node-sorting/placement
            if re.search(r"Total No of Active Cores", line):
                mic_cores = re.match(r"\s+Total No of Active Cores\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC Cores: " + mic_cores
                current_mic_attribute['mic_cores'] = mic_cores
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi Die Temperature.
            # NOTE: This will be better handled in PBS Pro 12.0 w/ PBS MOM Hooks
            # to periodically poll and update the server with the values. More importantly
            # we could detect overheating, and take the vnode out of the scheduling pool, etc.
            # Usage: MIC temperature (C), vnode-based, meta-data, node-sorting
            #if re.search(r"Die Temp", line):
            #    mic_temp = re.match(r"\s+Die Temp\s+: (\d+)", line).group(1)
            #    if DEBUGON:
            #        print "Current MIC Temperature: " + mic_temp
            #    current_mic_attribute['mic_temp'] = mic_temp
            #    current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi GDDR Density, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC density (Mb), vnode-based, requestable (memory?), node-sorting/placement
            if re.search(r"GDDR Density", line):
                mic_density = re.match(r"\s+GDDR Density\s+: (.*)", line).group(1).replace(" ", "").lower()
                if DEBUGON:
                    print "Current MIC GDDR Density: " + mic_density
                current_mic_attribute['mic_density'] = mic_density
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi GDDR Size, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC size (MB), vnode-based, requestable (memory?), node-sorting/placement
            if re.search(r"GDDR Size", line):
                mic_size = re.match(r"\s+GDDR Size\s+: (.*)", line).group(1).replace(" ", "").lower()
                if DEBUGON:
                    print "Current MIC GDDR Size: " + mic_size
                current_mic_attribute['mic_size'] = mic_size
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi GDDR Technology, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC technology, vnode0based, meta-data, grouping
            if re.search(r"GDDR Technology", line):
                mic_technology = re.match(r"\s+GDDR Technology\s+: (.*)", line).group(1)
                if DEBUGON:
                    print "Current MIC GDDR Technology: " + mic_technology
                current_mic_attribute['mic_technology'] = mic_technology
                current_mic['mic' + mic_id] = current_mic_attribute

            # Detecting Intel Xeon Phi GDDR Speed, and pushing to the
            # "current" mic attribute dictionary.
            # Usage: MIC speed (GT/s), vnode-based, requestable, benchmarking?, node-sorting/grouping
            if re.search(r"GDDR Speed", line):
                mic_speed = re.match(r"\s+GDDR Speed\s+: (\d+.\d+)", line).group(1)
                if DEBUGON:
                    print "Current MIC GDDR Speed: " + mic_speed
                current_mic_attribute['mic_speed'] = mic_speed
                current_mic['mic' + mic_id] = current_mic_attribute

        # For debugging purposes, this section of code will print to screen
        # all of the attributes of the Intel Xeon Phi device(s).
        if DEBUGON:
            print ""
            print "Global MIC Attributes: "
            for key, value in mic_global_attribute.iteritems():
                print key + " = " + value
            print "Number of Intel Xeon Phi Device(s): " + str(len(current_mic))
            print ""

            mic_counter = 0
            while (mic_counter < len(current_mic)):
                print ""
                print "Intel MIC Device ID " + str(mic_counter)
                for key, value in sorted(current_mic['mic' + str(mic_counter)].iteritems()):
                    print key + " = " + value
                mic_counter = mic_counter + 1
            print ""

        # Writing the Intel Xeon Phi attributes into the mic_vnodedef.cfg file
        # that defines the Intel Xeon Phi device(s) within PBS Professional.
        # The format of the mic_vnodedef.cfg file adheres to the Version 2
        # configuration file. See PBS Professional Admin Guide, section
        # "Creating Version 2 MOM Configuration Files" for more details.
        print "Constructing the mic_vnodedef file..."
        if not os.path.exists(os.environ['PBS_HOME'] + "/mom_priv/config.d"):
            os.makedirs(os.environ['PBS_HOME'] + "/mom_priv/config.d")
        mic_vnodedef_file = open(os.environ['PBS_HOME'] + "/mom_priv/config.d/mic_vnodedef", "w")
        mic_vnodedef_file.write("$configversion 2\n")
        mic_vnodedef_file.write(hostname + ": resources_available.ncpus = " + str(ncpus) + "\n")
        mic_vnodedef_file.write(hostname + ": resources_available.mem = " + memory + "\n")
        mic_counter = 0
        while (mic_counter < len(current_mic)):
            mic_vnodedef_file.write(hostname + "-mic" + str(mic_counter) + ": resources_available.nmics = 1\n")
            mic_vnodedef_file.write(hostname + "-mic" + str(mic_counter) + ": resources_available.mic_driver = " +\
                                    mic_driver + "\n")
            mic_vnodedef_file.write(hostname + "-mic" + str(mic_counter) + ": resources_available.mic_mpss = " +\
                                    mic_mpss + "\n")
            for key, value in sorted(current_mic['mic' + str(mic_counter)].iteritems()):
                mic_vnodedef_file.write(hostname + "-mic" + str(mic_counter) + ": resources_available." +\
                                        key + " = " + value + "\n")
            mic_vnodedef_file.write(hostname + "-mic" + str(mic_counter) + ": sharing = default_excl\n")
            mic_counter = mic_counter + 1
        mic_vnodedef_file.close()
        print "..... DONE!"
    else:
        print "ERROR: Could NOT find " + INTEL_MICINFO + ". Please verify that the Intel Xeon Phi\
        packages have been installed properly"
        print ""
        sys.exit(0)
else:
    print "Intel Xeon Phi package is NOT present... skipping setup and configuration."
    sys.exit(0)

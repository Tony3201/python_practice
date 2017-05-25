#!/usr/bin/python
import sys

print "123",
sys.stdout.softspace = 0
print ":456"


def sendH(sched_admin_req, host, opCode, cmd):
    host_name = host.get("HostName")
    sched_admin_req.setHost(host_name)
    print "%s <%s> ......" % (opCode, sched_admin_req.getHost()),
    response = comm.send_request_to_master(sched_admin_req, 'schedadmin')
    if response is not None:
        err_msg = response.get("ErrStr")
        err_no = response.get("ErrNo")
        if err_no == 0:
            print "done",

        if err_no != 0:
            if opCode is "Open":
                status = host.get("HStatus")
                if status & jhosts.HostStatus.BUSY:
                    print "done : host remains closed due to load threshold;",
                elif status & jhosts.HostStatus.FULL:
                    print "done : host remains closed due to job limit;",
                elif status & jhosts.HostStatus.WIN:
                    print "done : host remains closed due to dispatch window;",
                elif status & jhosts.HostStatus.LOCKED:
                    print "done : host remains closed due to being locked;",
                elif status & jhosts.HostStatus.LOCKED_MASTER:
                    print "done : host remains closed due to being locked by master",
                else:
                    print comm.i18n('%s.') % (ERRMSG[err_no]),
            else:
                print comm.i18n('%s.') % (ERRMSG[err_no]),

    else:
        print comm.i18n("Fail to %s.") % cmd,

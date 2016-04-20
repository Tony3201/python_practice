#!/usr/bin/env python
# coding=utf8

import httplib
import json


def sendRequest(data):
    # the following constants for integer status codes:
    OK = 200

    # master ip and port
    masterUrl = '192.168.0.95'
    masterPort = 6322
    httpClient = None
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        httpClient = httplib.HTTPConnection(masterUrl, masterPort, timeout=30)
        print httpClient
        httpClient.request('POST', '/', json.dumps(data), headers)

        response = httpClient.getresponse()
        print response.status
        print response.reason
        replyData = json.loads(response.read())

        if response.status == OK:
            return replyData
        else:
            print response.reason
            exit(0)

    except Exception, err:
        print err
        exit(0)
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':

    ReqData = {'Status': 0, 'NumMaxJob': 0, 'NumJob': 0, 'HostName': '', 'NumSsuspJob': 0, 'NumRunJob': 0, 'CmdOpcode': 41, 'ReqOpcode': 1, 'UserJobSlotsLimit': 0, 'NumReserve': 0}
    reply = sendRequest(ReqData)
    print reply

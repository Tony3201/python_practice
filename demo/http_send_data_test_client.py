#!/usr/bin/env python
# coding=utf8

import httplib
import json

class queryHostInfoReq:
    def __init__(self):
        self.HostName = ''
        self.Status = 0
        self.UserJobSlotsLimit = 0
        self.NumMaxJob = 0
        self.NumJob = 0
        self.NumRunJob = 0
        self.NumSsuspJob = 0
        self.NumReserve = 0

        self.CmdOpcode = 41
        self.ReqOpcode = 1

    # convert obj to dict for json encoding
    def convertObjToDict(self):
        dict = {}
        dict.update(self.__dict__)
        return dict



def sendRequest(data):
    # the following constants for integer status codes:
    OK = 200

    # master ip and port
    masterUrl = '192.168.0.95'
    masterPort = 6323
    httpClient = None
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        httpClient = httplib.HTTPConnection('192.168.0.95:6323', timeout=30)
        print masterUrl,masterPort
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

    HostInfoReq = queryHostInfoReq().convertObjToDict()
    sendRequest(HostInfoReq)

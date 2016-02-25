#!/usr/bin/env python
# coding=utf8

import httplib
import json


def sendRequest(data):
    # the following constants for integer status codes:
    OK = 200

    # master ip and port
    masterUrl = '192.168.3.121'
    masterPort = 8081
    httpClient = None
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        httpClient = httplib.HTTPConnection(masterUrl, masterPort, timeout=30)
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
    f = open('./testData')
    data = f.read()
    print len(data)
    ReqData = {'data': data}
    reply = sendRequest(ReqData)
    print reply
    print len(reply['data'])

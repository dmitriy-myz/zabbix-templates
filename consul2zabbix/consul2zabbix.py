#!/usr/bin/python

import sys
import json
import requests
import socket
import md5


nodeName = socket.gethostname()
#print nodeName

url = 'http://127.0.0.1:3004/v1/health/node/{0}'.format(nodeName)
#print url


def getUrl(url, cached = True):
    cacheFileName = md5.new(url).hexdigest()
    cacheFile = '/tmp/{0}'.format(cacheFileName)

    if cached:
        with open(cacheFile, 'r') as f:
            result = f.read()
    else:
        result = requests.get(url).text
        with open(cacheFile, 'w') as f:
            f.write(result)
    return result

def getDiscovery():
    discovery_list = {}
    discovery_list['data'] = []

    nodeServices = getUrl(url, False)

    services = json.loads(nodeServices)
    for service in services:
        if service['CheckID'] != 'serfHealth':
            #print service['Status']
            #print service['ServiceName']
            zbx_item = {"{#ServiceID}": service['ServiceID']}
            discovery_list['data'].append(zbx_item)
    print json.dumps(discovery_list, indent=4, sort_keys=True)


def getStatus(ServiceID):
    nodeServices = getUrl(url, True)
    services = json.loads(nodeServices)
    status = 0
    for service in services:
        if service['ServiceID'] == ServiceID:
            if service['Status'] == 'passing':
                status = 1
            else:
                status = 0
    print status

action = sys.argv[1].lower()
if action == 'discovery':
    getDiscovery()
elif action == 'status':
    serviceID = sys.argv[2]
    getStatus(serviceID)


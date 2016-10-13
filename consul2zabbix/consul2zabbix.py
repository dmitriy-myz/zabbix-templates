#!/usr/bin/python

import sys
import json
import requests
import socket
import md5


nodeName = socket.gethostname()
#print nodeName

url = 'http://127.0.0.1:8500/v1/health/node/{0}'.format(nodeName)
#print url


def getDiscovery():
    discovery_list = {}
    discovery_list['data'] = []

    nodeServices = requests.get(url).text

    services = json.loads(nodeServices)
    for service in services:
        if service['CheckID'] != 'serfHealth':
            #print service['Status']
            #print service['ServiceName']
            zbx_item = {"{#SERVICEID}": service['ServiceID']}
            discovery_list['data'].append(zbx_item)
    print json.dumps(discovery_list, indent=4, sort_keys=True)

def getStatus(ServiceID):
    nodeServices = requests.get(url).text
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


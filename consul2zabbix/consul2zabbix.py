#!/usr/bin/python

import sys
import json
import urllib2
import socket

# Set your token here
token = ''

if len(sys.argv) == 1:
    print("Usage: {} <discovery|status|nodeStatus> [serviceID]".format(sys.argv[0]))
    sys.exit(1)

headers = {'X-Consul-Token': token} if token else {}

nodeName = socket.gethostname()

url = 'http://127.0.0.1:8500/v1/health/node/{0}'.format(nodeName)

def getNodeServices():
    req = urllib2.Request(url, headers=headers)
    r = urllib2.urlopen(req)
    if r.getcode() != 200:
        print(r.getcode(), r.read())
        sys.exit(1)
    content = r.read()
    services = json.loads(content)
    return services

def serviceDiscovery():
    discovery_list = {}
    discovery_list['data'] = []
    services = getNodeServices()
    for service in services:
        if service['CheckID'] != 'serfHealth':
            zbx_item = {"{#SERVICEID}": service['ServiceID']}
            discovery_list['data'].append(zbx_item)
    print(json.dumps(discovery_list, indent=4, sort_keys=True))

def nodeStatus():
    nodes = getNodeServices()
    try:
        status = 1 if nodes[0]['Status'] == 'passing' else 0
    except Exception:
        status = 0

    print(status)

def getStatus(ServiceID):
    services = getNodeServices()
    status = 0
    for service in services:
        if service['ServiceID'] == ServiceID:
            if service['Status'] == 'passing':
                status = 1
            else:
                status = 0
    print(status)

action = sys.argv[1].lower()
if action == 'discovery':
    serviceDiscovery()
elif action == 'status':
    serviceID = sys.argv[2]
    getStatus(serviceID)
elif action == 'nodestatus':
    nodeStatus()

#!/usr/bin/python

import sys
import json
import requests
import socket
import md5

# Set your token here
token = None

if len(sys.argv) == 1:
    print("Usage: {} <discovery|status> [serviceID]".format(sys.argv[0]))
    sys.exit(1)

headers = {'X-Consul-Token': token} if token else {}

nodeName = socket.gethostname()

url = 'http://127.0.0.1:8500/v1/health/node/{0}'.format(nodeName)


def getDiscovery():
    discovery_list = {}
    discovery_list['data'] = []

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print r.status_code, r.text
        sys.exit(1)

    nodeServices = r.text

    services = json.loads(nodeServices)
    for service in services:
        if service['CheckID'] != 'serfHealth':
            zbx_item = {"{#SERVICEID}": service['ServiceID']}
            discovery_list['data'].append(zbx_item)
    print json.dumps(discovery_list, indent=4, sort_keys=True)

def getStatus(ServiceID):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print r.status_code, r.text
        sys.exit(1)

    nodeServices = r.text

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

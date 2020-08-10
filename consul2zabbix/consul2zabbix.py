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


consul_url = 'http://127.0.0.1:8500'

def getNodes():
    url = '{0}/v1/catalog/nodes'.format(consul_url)
    req = urllib2.Request(url, headers=headers)
    r = urllib2.urlopen(req)
    if r.getcode() != 200:
        print(r.getcode(), r.read())
        sys.exit(1)
    content = r.read()
    nodes = json.loads(content)
    nodes = list(map(lambda n: n['Node'], nodes))
    return nodes


def getNodeServices(nodeName):
    url = '{0}/v1/health/node/{1}'.format(consul_url, nodeName)
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
    nodes = getNodes()
    for node in nodes:
        services = getNodeServices(node)
        for service in services:
            if service['CheckID'] != 'serfHealth':
                zbx_item = {"{#SERVICEID}": service['ServiceID'],
                            "{#NODENAME}": node 
                            }
                discovery_list['data'].append(zbx_item)
    print(json.dumps(discovery_list, indent=4, sort_keys=True))

def nodeStatus(node):
    nodes = getNodeServices(node)
    try:
        status = 1 if nodes[0]['Status'] == 'passing' else 0
    except Exception:
        status = 0

    print(status)

def getStatus(ServiceID, node):
    services = getNodeServices(node)
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
    node = sys.argv[2]
    serviceID = sys.argv[3]
    getStatus(serviceID, node)
elif action == 'nodestatus':
    node = socket.gethostname()
    nodeStatus(node)

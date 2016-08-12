#!/usr/bin/python

import os
import re
import json

devices = os.listdir('/sys/class/hwmon')
discovery_list = {}
discovery_list['data']=[]

for device in devices:
    device_path = os.path.join('/sys/class/hwmon', device)
#    print device
    features = os.listdir(device_path)

    if 'name' not in features:
        continue

    with open(os.path.join(device_path,'name'), 'r') as s_name:
        device_name = s_name.read().replace('\n', '')
#        print device_name

    for feature in features:
        temp_sensor = re.search('^(temp\d+)_', feature)
        if temp_sensor:
            temp_sensor = temp_sensor.group(1)
            zbx_item = {"{#DEVICE_NAME}": device_name, "{#DEV_DIR}": device, "{#TEMP_SENSOR}": temp_sensor}
            if zbx_item not in discovery_list['data']:
#                print temp_sensor
                discovery_list['data'].append(zbx_item)
print json.dumps(discovery_list, indent=4, sort_keys=True)

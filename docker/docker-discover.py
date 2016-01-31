#!/usr/bin/env python
import json
import fileinput
data = []
for line in fileinput.input():
    line = line.strip()
    shasum = line.split(" ")[0]
    name = line.split(" ")[1]
    data.append({'{#SHASUM}': shasum, '{#NAME}': name})
#    print "shasum = ", shasum
#    print "name = ", name
print json.dumps({"data": data})



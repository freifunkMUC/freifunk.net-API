#!/usr/bin/env python

import json
import re
from datetime import datetime

json_data = open('freifunk.net.json')
data = json.load(json_data)
json_data.close()

f = open('node_stats','r')
numbers = re.findall(r'\d+', f.readline())
nodes = numbers[1]
# clients = numbers[2]

data["state"]["lastchange"] = datetime.now().isoformat('T')
data["state"]["nodes"] = nodes
print data["state"]["lastchange"]
print data["state"]["nodes"]

f = open('freifunk.net.json', 'w')
f.write(str(data))
f.close()

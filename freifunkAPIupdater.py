#!/usr/bin/env python

import json
from json import dumps
import re
from datetime import datetime

json_data = open('freifunk.net.json')
data = json.load(json_data)
json_data.close()

try:
  with open('node_stats', 'r') as fn:
    numbers = re.findall(r'\d+', fn.readline())
    nodes = numbers[2]
except Exception as ex:
  exit(ex)

data["state"]["lastchange"] = datetime.now().isoformat('T')
data["state"]["nodes"] = int(nodes)
print (data["state"]["lastchange"])
print (data["state"]["nodes"])

try:
  with open('freifunk.net.json', 'w') as fn:
    json.dump(data, fn, indent=4, ensure_ascii=False)
    fn.close()
except Exception as ex:
  exit(ex)

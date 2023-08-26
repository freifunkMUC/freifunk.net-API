#!/usr/bin/env python
import sys
import json
import re
import os
from datetime import datetime


for file in os.listdir("."):
    if file.endswith(".json"):
        with open(file, encoding="utf8") as json_data:
            data = json.load(json_data)
            json_data.close()

        try:
            with open('node_stats', 'r', encoding="utf8") as fn:
                numbers = re.findall(r'\d+', fn.readline())
                nodes = numbers[2]
        except OSError as ex:
            sys.exit(ex)

        data["state"]["lastchange"] = datetime.now(
        ).astimezone().replace(microsecond=0).isoformat()
        data["state"]["nodes"] = int(nodes)
        print(data["state"]["lastchange"])
        print(data["state"]["nodes"])

        try:
            with open(file, 'w', encoding="utf8") as fn:
                json.dump(data, fn, indent=4, ensure_ascii=False)
                fn.close()
        except OSError as ex:
            sys.exit(ex)

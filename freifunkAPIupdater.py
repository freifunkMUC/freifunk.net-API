#!/usr/bin/env python
import sys
import json
from datetime import datetime


file_path = "cities_to_nodes_urls.json"

# Das Dictionary aus der JSON-Datei laden
with open(file_path, "r") as file:
    cities_to_urls = json.load(file)

for city, url in cities_to_urls.items():
    #Load API json
    filenamecity = f"{city}.json"
    with open(filenamecity, encoding="utf8") as json_data:
        data = json.load(json_data)
        json_data.close()

    #Load Results json for Update
    filename_result = f"{city}-results.json"
    with open(filename_result, encoding="utf8") as json_resultdata:
        updatedata = json.load(json_resultdata)
        json_resultdata.close()
    
    nodes = updatedata["online_nodes"]

    data["state"]["lastchange"] = datetime.now().astimezone().replace(microsecond=0).isoformat()
    data["state"]["nodes"] = int(nodes)
    print(city)
    print(data["state"]["lastchange"])
    print(data["state"]["nodes"])
    try:
        with open(filenamecity, 'w', encoding="utf8") as fn:
            json.dump(data, fn, indent=4, ensure_ascii=False)
            fn.close()
    except OSError as ex:
        sys.exit(ex)
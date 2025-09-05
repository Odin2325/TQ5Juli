import json

name = 'Nicolas'

#'Nicolas' => "Nicolas"
name_json = json.dumps(name)

with open('name_json.json', 'w') as json_probe_datei:
    json_probe_datei.write(name_json)
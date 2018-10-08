import requests
import json
import csv
import Spielausgang

#pull first matchday data
spieltag = 1
response = requests.get('http://www.openligadb.de/api/getmatchdata/bl1/2018/%2d' % (spieltag))


print(response.status_code)

#write a json file
eintrag = response.content #Api-Inhalt in eintrag speichern
with open ('%2d matchday.json' % (spieltag),'w') as dataFile:
    json.dump(eintrag, dataFile) #erstellt json Datei


print eintrag

#pretty json
'''
parsed = json.loads(eintrag2)
print json.dumps(parsed, indent=2, sort_keys=True)
'''










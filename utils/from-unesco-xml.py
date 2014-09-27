import urllib.request
import xmltodict
import json

# xmldata = urllib.request.urlopen('http://whc.unesco.org/en/list/xml').read()
xmldata = open('/home/jordan/django/unesco_project/data/xml').read()
doc = xmltodict.parse(xmldata)
row = doc["query"]["row"][0]
for r in doc["query"]["row"]:
    print (r["id_number"])


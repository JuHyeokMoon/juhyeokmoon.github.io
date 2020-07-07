import json

jstring = open('myjsonfile.json','r').read()
jsonData = json.loads(jstring)

print(type(jsonData))
print(jsonData)
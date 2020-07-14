import json

#객체를 .read()해서 string 문자형으로 입력 
jstring = open("myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

# print(type(jsonData)) 
# print(jsonData)

for item in jsonData:
    item["maxTemp"] = float(item["maxTemp"])
    print(item)

maxTemp = 0
maxTempdate = ""

for item in jsonData:
    if maxTemp < item["maxTemp"]:
        maxTempdate = item["date"]
        maxTemp = item["maxTemp"]

print(maxTemp)
print(maxTempdate)
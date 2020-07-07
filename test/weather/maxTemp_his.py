import json
import matplotlib.pyplot as plt

jstring = open("myjsonfile.json", "r").read()
jsonData = json.loads(jstring)

maxTempList = []

for item in jsonData:
    item["maxTemp"] = float(item["maxTemp"])
    maxTempList.append(item["maxTemp"])

plt.hist(maxTempList, bins=50, color='b')
plt.show()
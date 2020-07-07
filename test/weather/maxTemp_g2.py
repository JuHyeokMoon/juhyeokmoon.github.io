import json
import matplotlib.pyplot as plt

jstring = open("myjsonfile.json", "r").read()
jsonData = json.loads(jstring)
#print(jsonData)

maxTempList = []

#매월 1일 데이터로 그래프를 그리는
for item in jsonData:
    if item["date"].split('-')[2] == '01':      #split() -단위로 쪼개 리스트 반환 [0]:2019, [1]:01, [2]:01
        item["maxTemp"] = float(item["maxTemp"])
        maxTempList.append(item["maxTemp"])

plt.plot(maxTempList, 'r')
plt.show()
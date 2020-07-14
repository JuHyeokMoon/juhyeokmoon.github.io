import csv
import matplotlib.pyplot as plt

f = open('test/population/202006_202006_연령별인구현황_월간_남여.csv')
data = csv.reader(f)

m = []
f = []

for row in data:
    if '전국' in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3].replace(",", "")))
            f.append((int(row[-(i+1)].replace(",", "")))*-1)
f.reverse()     #리스트 순서 전부 뒤집기

summ = sum(m)
sumf = sum(f)
size = [summ, (sumf*-1)]

plt.rc('font', family='Malgun Gothic')
plt.title('대한민국 2020 6월 인구분포')
color = ['r', 'b']
plt.axis('equal')
# plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors=color)
plt.pie(size, labels=['남', '여'], autopct='%.1f%%',
        colors=color, startangle=90, explode=(0, 0.1))      #explode 는 가운데에서 조금 띄워 달라, startangle은 각도 조절

plt.legend()
plt.show()

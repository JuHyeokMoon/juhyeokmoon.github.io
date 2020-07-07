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
            f.append((int(row[-(i+1)].replace(",", "")))*-1)    #그래프를 역전 시켜서 따로 보여주고 싶음, *-1로
f.reverse()

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('대한민국 2020 6월 인구분포')
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.legend()
plt.show()

import csv
f = open('test/population/202006_202006_연령별인구현황_월간_남여.csv')
data = csv.reader(f)

m = []
f = []

for row in data:
    if '전국' in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3].replace(",", "")))
            f.append(int(row[-(i+1)].replace(",", "")))

# if '전국' in row[0]:
#     for i in row[3:104] :
#         m.append(int(i))
#     for i in row[106:] :
#         f.append(int(i))

print(m)
print(f)
f.reverse()  #여자 데이터는 100부터 0으로 나이가 거꾸로 되어 있어 역전 시킴
print(f)

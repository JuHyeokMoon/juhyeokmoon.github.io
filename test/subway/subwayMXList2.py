import csv
f = open('test/subway/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

mx = [0] * 4                #mx = [] 와 mx[0]*4 차이
mx_station = [''] * 4       #MXList 와는 다르게 리스트 공간을 선언 해줌으로 인덱스를 가지고 접근할 수 있다.
label = ['유임승차', '유임하차', '무임승차', '무임하차']
for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
        if row[i] > mx[i-4]:
            mx[i-4] = row[i]
            mx_station[i-4] = row[3]+''+row[1]

for i in range(4):
    print(label[i]+' : '+mx_station[i], mx[i])

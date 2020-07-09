import csv
f = open('test/subway/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

mx = 0
rate = 0
mx_row = []
for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0:             #에러 처리 
        rate = row[4]/row[6]    #무임승차 대비 유임승차비율이 가장 높은 역
        if rate > mx:
            mx = rate
            mx_row = row

print(mx)
print(mx_row)

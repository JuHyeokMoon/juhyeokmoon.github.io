import csv
f = open('test/subway/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

for row in data:
    if data.line_num == 1:      # 한라인을 읽을때마다 증가, 하지만 반드시 row를 의미하는건 아님
        continue
    for i in range(4, 8):       # 4~8열에 데이터들 ,를 제거하고 정수형으로 변환
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    print(row)

import csv

f = open('test/subway/2020년 06월  교통카드 통계자료2.csv')
data = csv.reader(f)

mx = 0
mx_station = ''
for row in data:
    if data.line_num < 3:
        continue
    for i in range(4, 51):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    # if sum(row[10:15:2]) > mx:        #승차만 7시 8시 9시 합
    #     mx = sum(row[10:15:2])
    #     mx_station = row[3] + '(' + row[1] + ')'

    # if sum(row[11:16:2]) > mx:
    #     mx = sum(row[11:16:2])
    #     mx_station = row[3] + '(' + row[1] + ')'

    t = 23                  #23시에 가장 탑승 인원이 많은 역
    a = row[4+(t-4)*2]

    # s_t = 9               #9시부터 18시까지 탑승 인원이 가장 많은 역
    # e_t = 18
    # a = sum(row[(2*(s_t-2)):(2*(e_t-2)):2])
    if a > mx:
        mx = a
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)

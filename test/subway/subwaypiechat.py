import csv
import matplotlib.pyplot as plt

f = open('test/subway/2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)
label = ['유임승차', '유임하차', '무임승차', '무임하차']
for row in data:
    if data.line_num == 1:  #첫번째 라인은 속성이고
        continue
    if data.line_num == 3:  #두번째 라인부터 데이터인데 한 행만 가져와서 그래프 그릴거다.
        break
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])

    plt.figure(dpi=150)
    plt.rc('font', family='Malgun Gothic')
    plt.title(row[3]+''+row[1])
    plt.pie(row[4:8], labels=label, autopct='%1.f%%')  #autopct 그래프 안에 값 단위 설정
    plt.axis('equal')
    plt.savefig('test/subway/'+row[3]+''+row[1]+'.png')
    plt.show()

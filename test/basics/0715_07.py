#연습문제3
#요일 출력

import datetime

def date(a,b):
    w = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    n = datetime.date(2020,a,b).weekday()
    print(f'{w[n]}')

a, b = map(int, input('월과 일을 입력 : ').split())
date(a,b)





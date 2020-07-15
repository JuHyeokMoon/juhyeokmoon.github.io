#연습 문제
#정수 부분과 실수 부분 나눠서 출력 

def fl(number):
    i_n=int(number)
    print(f'정수 : {int(number)}')
    print(f'실수 : {round(number-i_n,2)}')

num = float(input('Enter float(.2) >> '))
fl(num)


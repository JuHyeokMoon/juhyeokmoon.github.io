#약수 구하는 프로그램

#1,2,5,7

def divisor(num, *me) :
    # for i in range(1, num+1):
    #     if num % i == 0:
    #         return num
    for i in me :
        print(f"{i}", end='')
    divi = [x for x in range(1, num+1) if num % x ==0]
    return divi

if __name__ == "__main__" :
    while True :
        num = int(input('Enter Num : '))
        if num <= 0 :
            print('Program error')
            break
        else :
            result = divisor(num, "010-0000-0000", "H.R", "Moon")
            print('\n{}약수는 {}'.format(num,result))

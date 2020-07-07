#제곱근 판별
import math

def root(n):
    result = math.sqrt(n)
    if result - int(result) == 0 :
        return result
    else :
        return -1
if __name__ == '__main__':
    while True :        
        num = int(input("Enter number >> "))
        if num == 0 :
            break
        elif num < 0 :
            break
        else :
            print(f'{num}의 제곱근은 {root(num)}')
# n ~ m 범위의 소수 구하기
import math

n, m = [int(i) for i in input("input number >> ").split()]
if n<=1 or m<=1 or n>m : print("Wrong Number!")
prime_list = []
count = 0
for i in range(n,m+1):
    for j in range(2,i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        prime_list.append(i)
    count = 0
print(prime_list)


#에라토스테네스의 체를 이용한 방법
def prime(num):
    if num == 1 : return False
    n=int(math.sqrt(num))

    for i in range(2,n+1):
        if num % i == 0 :return False
    return True

# print(~~)
import random

num = int(input("Enter Num >> "))

def deletion(a):
    length = len(a)
    a.remove(min(a))
    if length == 0 :
        result=a.append(-1)
        print(f'{result}')
    else :
        print(f'{a}')
if num > 0 :
    d = [ random.randint(1,100) for i in range(0,num) ]
    print(type(d))
    deletion(d)
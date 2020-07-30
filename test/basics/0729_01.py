#3진법 문제

def third (n):
    result = 0
    r = n//3
    v = n%3
    int(r)
    if v == 0 :
        result = str(r)+'4'
    elif v == 1 :
        result = str(r)+'1'
    elif v == 2 :
        result = str(r)+'2'
    return result
    
num = int(input("Enter number :"))
print(third(num))

# q,r = divmod(q,3)     나머지와 몫을 반환해주는 함수 
#멀티플라이 함수

def multiply(*var):
    result = 1
    for num in var :
        result = result * num
    return result

print(multiply(1,2,3))
print(multiply(5,8))
print(multiply(1,2,6,8))
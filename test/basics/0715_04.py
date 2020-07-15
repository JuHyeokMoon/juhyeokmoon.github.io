#Decorator

# def null_hi(obj):
#     name = input('input your name >>')
#     print(f'{name}',end='')
#     return obj

# @null_hi
# def greet():
#     return 'hello'

# print(greet())

##################

def uppercase(obj):
    def wrapper():
        origin_result = obj()
        modi_result = origin_result.upper()
        return modi_result
    return wrapper
@uppercase
def greet():
    return 'Hello'
@uppercase
def hi():
    return f'Longtime no see'

print(greet())
print(hi())
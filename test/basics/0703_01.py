#파이썬을 파이썬 답게 사용
#제너레이터

import sys
gen = [ i for i in range(50000) if i%2 ==0]
print(f'gen type: {type(gen)}')
print(f'memory of gen : {sys.getsizeof(gen)}')
# for i in gen:
#     print(f'i : {i}')


gen2 =  (i for i in range(50000) if i%2 ==0)
print(f'gen2 type: {type(gen2)}')
print(f'memory of gen2 : {sys.getsizeof(gen2)}')
# for i in gen:
#     print(f'i : {i}')
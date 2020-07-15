from collections import deque

dq = deque()
item = ['berry','banana']
dq.append('apple')
dq.appendleft('pear')
dq.appendleft(item)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

item = ['cherry','mango']
dq.extend(item)
print(dq)
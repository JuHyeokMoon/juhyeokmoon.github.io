#Math 모듈 사용
import math as m
radian = m.radians(30)
print("sind(30) : {}".format(m.sin(radian)))
print("sind(30) : {:.2f}".format(m.cos(radian)))
print("sind(30) : {:5.1f}".format(m.tan(radian)))

print(m.floor(3.2))
print(m.ceil(3.2))

print(m.log(2.718))
print('%0f' % m.log(2.718))
print(m.log(1000,10))
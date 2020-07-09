#실습 클래스 작성 point 이동 

class Point:
    def __init__(self,x,y):
        self.x_point = x
        self.y_point = y
    def setx(self, x):
        self.x_point = x
    def sety(self, y):
        self.y_point = y
    def movexy(self,dx,dy):
        self.x_point += dx
        self.y_point += dy
    def getxy(self):
        return self.x_point , self.y_point

mypoint= Point(0,0)
print(mypoint.getxy())
mypoint.setx(10)
mypoint.sety(10)
print(mypoint.getxy())
mypoint.movexy(10,-5)
print(mypoint.getxy())
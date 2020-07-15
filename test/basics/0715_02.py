#descriptor

class Youclass:
    def __init__(self, val=None, name='you'):
        self.val = val
        self.name = name
    def __get__(self, obj, objtype):
        print(f'YouClass, {self.name}')
        return self.val
    def __set__(self, obj, val):
        print(f'ReBinding, {self.name}')
        self.val = val
class MeClass :
    x = Youclass(100,'x')
    y =5

me = MeClass()
print(me.x)
me.x=200

#property
#getter, setter, delete 메소드를 가지고 있음

#@property
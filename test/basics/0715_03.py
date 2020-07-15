#@property

class Property_test:
    def __init__(self,name):
        self._name = name       #self._name _가 없으면 안됨
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_v):
        self._name = name_v

me = Property_test('Korea')
print(me.name)
me.name = 'Industrial'
print(me.name)















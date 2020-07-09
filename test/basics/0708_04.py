class Employee:
    def __init__(self, name, sal):
        self._name = name
        self._salary = sal
    
    def _access(self,num):
        self.result= sum(num)
        self.total = self._salary + self.result
    
class Bank_employee(Employee):
    def bank_salary(self,tax):
        self._tax = tax
        self._pay = self._salary*self._tax

if __name__ =='__main__':
    me = Bank_employee('Yoon',30000)
    me._access([1000,2000,4000])
    print(f'{me.total}')
    print(f'{me._name},{me._salary}')
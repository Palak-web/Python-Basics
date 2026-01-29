class employee:
    def __init__(self):
        self.__name = "Palak"
    
a = employee()

# print(a.__name) #cannot be access accessed directly
print(a._employee__name) #can be eccessed indirectly

class Student:
    def __init__(self):
        self._name = "Harry"    #protected method
        
    def _funName(self):
        return "CodeWithHarry" 
    
class subject(Student):    #inherited class
    pass

obj = Student()
obj1 = subject()

print(obj._name)
print(obj._funName())

#calling by obj of student class
print(obj1._name)
print(obj1._funName())
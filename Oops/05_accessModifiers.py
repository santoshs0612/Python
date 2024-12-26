#private __

class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.__name) # can not be accessed directelly

# accesed indirectilly
# print(a._Employee__name)

# print(a.__dir__())

# protected 
# _
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"


obj = Student()

print(dir(obj))

print(obj._name)
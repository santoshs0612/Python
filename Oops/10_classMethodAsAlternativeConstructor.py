
class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])



e = Employee("Santosh", 120000)

print(e.name)
print(e.salary)

# If we have a sting as argumnet 
a = "Snatosh-12000"
e2 = Employee(a.split("-")[0],a.split("-")[1])
# b = a.split("-")
# print(b)

print(e2.name)
print(e2.salary)

#  To Handle this situation of split we can construct 
# a class method 

string = "BIlok-33294343"
e3 = Employee.fromStr(string)
print(e3.name)
print(e3.salary)

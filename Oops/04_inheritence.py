class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id= id
    
    def showDetails(self):
        print(f"The Name of Emplyee: {self.name} is {self.id}")
    


class Programmer(Employee):
    def showLanguage(self):
        print("The Default Language is Python")
e = Employee("Gupta ji",123)
e.showDetails()

p = Programmer("Santosh",242342)
p.showDetails()
p.showLanguage()
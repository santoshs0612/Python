# instance Varible and class varible 

class Employee:
    companyName = "Apple"
    noOfEmployee =0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        self.noOfEmployee +=1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} raise amount in {self.companyName} and total employee {self.noOfEmployee} has rsie {self.raise_amount}")


# emp1 = Employee("Santosh")
# # emp1.showDetails()
# Employee.showDetails(emp1)

emp1 = Employee("Santosh")
emp1.showDetails()
emp1.raise_amount =0.3
emp1.companyName ="Apple India"
Employee.companyName ="Google"
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()


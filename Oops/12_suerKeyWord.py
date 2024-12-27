class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
santosh = Programmer("Harry", "2345", "Python")
print(santosh.name)
print(santosh.id)
print(santosh.lang)


class ParentClass:
    def parent_method(self):
        print("This is the Parent Method 1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Santosh2")
        super().parent_method()
    def child_method(self):
        print("This is the child Method 2")
        super().parent_method()


# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

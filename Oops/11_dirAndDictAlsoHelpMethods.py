# dir() method , and __dict attribute

x = [1,2,3,4]

# print(dir(x))
# print(x.__add__)

y = (1,2,3,4,5)
# print(dir(y))
# print(y.__add__)

class Persion:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1

a = Persion("Santosh",23)
print(a.__dict__)
print(help(Persion))
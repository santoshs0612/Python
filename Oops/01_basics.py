# class Person:
#     name = "Santosh"
#     occupation = "Software Developer"
#     networth =10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# self is the current instance of the class 

# a = Person()
# a.name="Shubham"
# a.occupation = "Accountant"

# print(a.name,a.occupation)

# a.info()

# b =Person()
# b.info()

#  constructors 

class Person:

    def __init__(self,name,occupation):
        # print("Hey I am a Persion ")
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Santosh","Engineer")
a.info()
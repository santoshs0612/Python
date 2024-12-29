# Walrus Operator 
a =True
print(a :=False)

number = [1,2,3,4,5]

while (n :=len(number)) >0:
    print(number.pop())


# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = False
print(happy)

print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

#   Another Way with Walrus operator 
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
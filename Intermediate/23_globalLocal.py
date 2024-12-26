# x =4
# print(x)

# def hello():
#     x =5
#     print(f"The local x is {x}")
#     print("Hello Santosh")

# print(f"The Global x is {x}")
# hello()
# x =5
# print(f"The Global x is {x}")

x =10 
def my_fun():
    global x 
    x =4
    y =5
    print(y)

my_fun()
print(x)
# print(y)

def greet(fx):
    def mfx():
        print("Good Morning!")
        fx()
        print("Thanks for using this functions")
    return mfx


@greet
def hello():
    print("Hello World")
#  using decorators for the functions having arguments 
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning!")
        fx(*args,**kwargs)
        print("Thanks for using this functions")
    return mfx


@greet
def add(a,b):
    print(a+b)

hello()
# or
# greet(hello)() #we dont need to use @greet before the functions 

# greet(add)(1,2)
add(1,2)

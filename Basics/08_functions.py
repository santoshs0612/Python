
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

calculateGmean(7,8)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

isGreater(3,5)

def isLesser(a,b):
   pass # dont do any thing 

# def average(a=9,b=1):
#    print("The avg is: ", (a+b)/2)

# average(4,6)
# average(b=9)

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)

average(5,6) # taking numbers as tuple 

# taking argument as dictionary 


def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")
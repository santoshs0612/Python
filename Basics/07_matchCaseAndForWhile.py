
# x = int(input("Enter the value of X: "))

match x:

    case 0:
        print("X is Zero")
    case 1:
        print("X is one")
    case _ if x!=3:
        print("It is Not three")
    case _:
        print("Anoter Number")

#  ============ For Loops +++++++++++++++++++

# name = 'Abhishek'
# for i in name:
#   print(i)
#   if(i =="b"):
#     print("This is something special!")
    
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#   print(color)
#   for i in color:
#     print(i)

# for k in range(5):
#   print(k + 1)
  
# for k in range(1, 20001):
#   print(k)

  
for k in range(1, 12, 3):
  print(k)
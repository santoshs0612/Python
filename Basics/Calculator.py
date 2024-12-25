

# Making a calculator 






def calculatior(val):
    if val == "1":
        print("Sum of a and b is a+b",a+b)
    if val == "2":
        print("Subsctraction of a and b is a-b",a-b)
    if val == "3":
        print("Multiplication of a and b is a*b",a*b)
    if val == "4":
        print("Division of a and b is a/b",a/b)
    if val == "5":
        print("Modulo of a and b is aModb",a%b)
    if val == "6":
        print("Division of a and b is a/b",a+b)


while(True):
    a = (int)(input("Enter First Value "))
    b= (int)(input("Enter Second Value "))

    print("Choose the operation you want to perform\n")
    print("Enter 1 for addintion")
    print("Enter 2 for substradction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for division")
    print("Enter 5 for Modulo")
    print("Enter 6 to get interger divion")
    print("Enter 0 to exit")
    val= input("Choose One Option ")
    if val=="0":
        break
    calculatior(val)




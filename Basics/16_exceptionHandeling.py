# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")


# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index out of bound")

# ========== Finally Clause ===========>

#  must executed code part 

# try:
#     l = [1,5,6,8]
#     i =int(input("Enter the Index: "))
#     print(l[i])
# except:
#     print("some eror occured ")
# # finally:
# #     print("Im always executed")

def func1():
    try:
        l = [1,5,6,8]
        i =int(input("Enter the Index: "))
        print(l[i])
    except:
        print("some eror occured ")
    finally:
        print("Im always executed")

# x = func1()
# print(x)

#   ====== Raising Custom error  ======>

a = int(input("ENter any vlaue between 5 and 9 "))

if(a< 5 or a>9):
    raise ValueError("Value should be between 5 and 9")


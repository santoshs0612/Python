# string 
name = "Santosh"
friend = "Murali"
anotherFriend = "Sudhunshau"

apple = """He said
i wanto to meet 
where?
Delhi?
no
why?

 """

# print("Hello, ",  name)
# print(apple)

# String is like aray of char 
# print(name[0])

# for c in name:
#     # print(c)


# ===========Slicing ==========================

# print(name[0:3])
# print(name[:5])
# print(name[3:4])
# # length method 
# print(len(name))
# print(name[0:-3])
# print(name[-3:])


# ============Methods in string =========

# String are immutable

a = "Sant osh!!!!!!! !!!!!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())

print(a.rstrip("!"))

print(a.replace("Santosh","Bilok"))

print(a.split(" ")) # return list 

blogHeading = "introduction to Java script"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith("!!!"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("to",4,10))

str1 = "he's Name is Don. He is an honnest Man"

print(str1.find("is"))
# print(str1.index("isff"))

str1 = "WelconeToConsole"
print(str1.isalnum())
str1 = "Welecome"
print(str1.isalpha())
print(str1.islower())

str1 = "We wish yo aMErry Christmas"
print(str1.isprintable())

str2 = "     "
print(str2.isspace())

# Swap Case
str3 = "Python is a Interpreted Language"

print(str3.swapcase())

print(str1.title())

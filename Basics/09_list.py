marks = [3, 5, 6,"Santosh", 4,7,8, 9, 10]

# print(marks)
# print(type(marks))

# print(marks[-3])
# print(len(marks))


# if 6 in marks:
#     print("Marks present")
# else:
#     print("Not Present")

# if "sa" in "santosh":
#     print("Yes present")


# for m in marks:
#     print(m)

print(marks[1:-1])
print(marks[1:4:3])

# list comprehension 
lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(4) if i%2==0]
print(lst)

#  list methods 

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(100)
print(l)

l.sort()
print(l)
l.sort(reverse=True)
print(l)

l.reverse()

print(l)

# print(l.index(100))
# print(l.count(1))
print(l)


# it will create deep copy so it will change the original fuicntio
# m = l
# m[0]=0
# print(l)

m = l.copy()
m[0]=0
print(l)
print(m)

l.insert(1,899)
print(l)

m = [900,1000,110]
l.extend(m)
print(l)

k =l+m
print(k)
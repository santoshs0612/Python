# tuple

tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup))
print(tup)
# tup[0]=90
print(tup[0])

# for i in tup:
#     print(i)
print(len(tup))

if 342 in tup:
    print("Yes Present ")


tup2= tup[1:4]

print(tup2 )

#  Operations on Tuple

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)

res  = tuple1.count(3)
print(res)
print(tuple1.index(3))


res = tuple1.index(3,4,8)
print(res)
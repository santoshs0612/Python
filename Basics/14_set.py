
set1= {1,3,4,5,1}

print(type(set1))
print(set1)

info = {"Santosh", 1,3,4,"hello"}
print(info)

santo = {}
print(type(santo))

santo = set()
print(type(santo))

for val in info:
    print(val)


# ======Methods in set =====>

s1 = {1,2,5,6}
s2 ={3,4,6,7}

print(s1.union(s2))

# s1 update  
print(s1.update(s2))

print(s1)

print(s1.intersection(s2))

# not common 
print(s1.symmetric_difference(s2))

print(s1.difference(s2))


# disjoint 

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s2.issubset(s1))

#  adding items 
s1.add(0)
print(s1)
s1.discard(0)
print(s1)

s1.pop()
print(s1)
del s1
s2.clear()
print(s2)
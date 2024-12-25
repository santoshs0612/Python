info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())
print(info.get("eligible"))
# print(info["jfd"])


for key in info.keys():
    print(info[key])
    print(f"The value correspond {key} is : {info[key]}")

for key ,value in info.items():
    print(f"The value correspond {key} is : {value}")

# ======Methods in dictionary ==========>

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()
# del ep1
# del ep1[122]
print(ep1)



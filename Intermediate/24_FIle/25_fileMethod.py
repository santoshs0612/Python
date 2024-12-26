
# f = open('/workspaces/Python/Intermediate/24_FIle/marks.txt',"r")

# i=0
# while True:
#     line = f.readline()
#     if not line:
#         break
#     i = i+1
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of Student {i} in Math is: {m1*2}")
#     print(f"Marks of Student {i} in SST is: {m2*2}")
#     print(f"Marks of Student {i} in Sports is: {m3*2}")
#     print(line)

    

# write lines 

f = open("myfile1.txt","w")

lines = ["line 1\n","line 2\n","line 3\n"]

f.writelines(lines)
f.close()
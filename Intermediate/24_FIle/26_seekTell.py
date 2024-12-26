# with open("/workspaces/Python/Intermediate/24_FIle/file.txt","r") as f:
#     print(type(f))
#     # move 10 bytes in the file 
#     f.seek(10)
#     # Read the next 5 bytes from 10th bytes 
#     print(f.tell()) # telling where we are in the file position 
#     data = f.read(5)
#     print(data)


with open("/workspaces/Python/Intermediate/24_FIle/sample.txt","w") as f:
    # print(type(f))
    f.write("Hello World")
    f.truncate(5)# make file only for 5 bytes 

with open("/workspaces/Python/Intermediate/24_FIle/sample.txt","r") as f:
    # print(ty
    print(f.read())

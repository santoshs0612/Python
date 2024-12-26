
# f = open('/workspaces/Python/Intermediate/24_FIle/myFile.txt',"r")

# print(f)
# text = f.read() # reading a file 

# # write()
# # append()
# # 
# print(text)
# f.close()

# f = open("/workspaces/Python/Intermediate/24_FIle/hello.txt", "w")

# f.write("Hello Satosh How arwe you?")
# f.close()


# with "with statement we need not to close a file 

with open("/workspaces/Python/Intermediate/24_FIle/hello.txt","a") as f:
    f.write("hey iam inside hello file")
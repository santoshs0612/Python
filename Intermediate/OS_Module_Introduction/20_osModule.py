import os


print(os.getcwd())

if not os.path.exists("/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials"):
    os.mkdir("/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials")

for i in range(1,3):
    os.mkdir(f"/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials/Day{i+1}")
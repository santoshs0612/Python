import os 
folders = os.listdir("/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials")

print(os.getcwd())
os.chdir("/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"/workspaces/Python/Intermediate/OS_Module_Introduction/Tutorials/{folder}"))
    
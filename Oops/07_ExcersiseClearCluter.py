# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

# clearing clutter assignment x
# /home/santosh/Desktop/Python/Python
import os 


# function taking directiory name and extension you want to change
def clearingClutter(directiory, extension):
    # print(os.getcwd())
    folder = os.listdir(directiory)

    # print(folder)

    # extension = ".png"
    for index,image in enumerate(folder):
        if(image.endswith(extension)):
            print(image)
            os.rename(f"/home/santosh/Desktop/Python/Python/Oops/Clutter/{image}",f"/home/santosh/Desktop/Python/Python/Oops/Clutter/{index+1000}{extension}")






print("Welcome to the clearing Clutter System ")
d = "/home/santosh/Desktop/Python/Python/Oops/Clutter"
clearingClutter(d,".jpeg")
print(f"We have changed the names of given files in given dir:{d}")

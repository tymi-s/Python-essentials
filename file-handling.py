# key function is open(). It takes two arguments:
# file name and mode


#available modes:
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

#specifying if we want binary form:
# "b" - Binary - Binary mode (e.g. images)
x = open("binay.txt","wb")
z = open("text.txt","w")



#reading a file:

#read()
file = open("example.txt","r")

q = file.read()
print(q)# prints whole file

# reading file with word with():

with open("example.txt","r") as f:
    print(f.read())

# using with makes it so that we don't need to close the file

#reading only part of file:
with open("example.txt","r") as f1:
    print("\n\n")
    print(f1.read(5))

#reading lines:

with open("example.txt","r") as f2:
    print(f2.readline())# returns a str
    print(type(f2.readline()))

# saving lines to list

with open("example.txt", "r") as f2:
    print(f2.readlines())  # returns a list
    print(type(f2.readlines()))


print("\n\nLOOP!!!!!!!\n")
#using loop to read a file
with open("example.txt", "r") as f3:
    for x in f3:

        print(x)

#WRITING/ CREATING A FILE:


with open("writing.txt", "w") as f4:#overwriting!
    f4.write("THIS IS A FIRST LINE TO ADD\n")

with open("writing.txt", "r") as f4:
    print("\n\n\n")
    print(f4.readlines())






##################deleting a file:
# to delete a file we need os module
import os

with open("todelete.txt","w") as f:
    f.write("NOOOOO  I WILL BE DELETED!")

# os.remove("todelete.txt")

#deleting if path exists:

if os.path.exists("todelete.txt"):
    os.remove("todelete.txt")
    print("Files was succesfully removed")
else:
    print("no such file was found")



#removing a folder - IT HAS TO BE EMPTY!!!:

if os.path.exists("folder_to_remove"):
    os.rmdir("folder_to_remove")
    print("FOLDER REMOVED!")
else:
    print("no such folder was found")



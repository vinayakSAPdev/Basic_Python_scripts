# #file handling concepts
# #opening a file
# file = open("example.txt", "r")  # "r" for read mode   
# content = file.read()
# print(content)
# file.close()

# #writing to a file
# file = open("example.txt", "w")  # "w" for write mode
# file.write("Hello, this is a new line.\n")
# file.write("This file is created using Python.")
# file.close()

# #appending to a file
# file = open("example.txt", "a")  # "a" for append mode  
# file.write("\nThis line is appended to the file.")
# file.close()


#reading a file line by line
# f = open("demotext.txt")
# print(f.read())
# f.close()

# #instead of using f.close() we can use with statement to automatically close the file after its block of code is executed
# with open("demotext.txt") as f:
#     print(f.read()) 

#Read Only Parts of the File
with open("demotext.txt") as f:
    print(f.read(10))  # Read the first 10 characters

#Read Lines into a List
with open("demotext.txt") as f:
    lines = f.readlines()
    print(lines)

#write text into the file using with statement
#w will overwite the existing content of the file and a will append to the existing content of the file
with open("demotext.txt", "w") as f:
    f.write("This is a new line of text.\n")
    f.write("This file is created using Python's with statement.")

#create a new file and write some text into it
with open("newfile.txt", "w") as f:
    f.write("This is a new file created using Python.\n")
    f.write("It contains some sample text.")


#Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("newfile.txt")

#To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The file does not exist")    

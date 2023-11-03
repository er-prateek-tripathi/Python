import os

'''
# reading files
path = "E:\\test.txt"
path1 = "E:\\Newfolder"

if os.path.isdir(path1):
    # checks if given path leads to a directory
    print("The path leads to a directory")

if os.path.exists(path):
    print("The file Exists!!")
    if os.path.isfile(path):
        print("This path contains a file.")
else:
    print("File doesn't Exist!!")

# Copying files

# if file is in some other directory, full file path is required
# while using with keyword, you do not need to close the file separately
# r - read, w - write. a - append
with open('D:\\Programming\\Python\\Self Learning\\test.txt', 'r') as file:
    print(file.read())

text = "I am a failure!!"

text3 = "\nTrying to make a change.\nDon't know how long it's going to take.\n" \
       "Just trying my best."

# if file is already available
text2 = "Opps! the text has been overwritten!!"

with open('text1.txt', 'w') as file1:
    file1.write(text2)

with open('text1.txt', 'a') as file2:
    file2.write(text3)

import shutil
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and o=modification times)

shutil.copyfile('test.txt', 'copy.txt')  # args = source, destination
# we can use different destination for creating copy file.
'''

# moving files



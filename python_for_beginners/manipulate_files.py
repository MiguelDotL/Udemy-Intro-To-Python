# # -------- FROM TERMINAL --------
# # ---- Make a new file ----
# file = open("filePath/goes/here.ext", 'w')
# # Overwrite existing text to file
# file.write("Add text to file from python")
# file.close()
#
# # ---- Cat the content of the file ----
# fileContent = file.read()
# file.close()
#
# print(fileContent)
#
# # ---- Append text to a file ----
# file = open("filePath/goes/here.ext", 'a')
# file.write("\n this is a new line in the same file")
# file.close()


# # ---- Using with / as ----
with open("filePath/goes/here/ext", 'w') as file:
    file.write("Using the 'with' method")



ids = ['b3','\nb4','\nb5','\nb6']

# with open("/home/spliff/Documents/code/udemy/python-for-beginners/python-for-beginners", 'a') as file:

ids = ['b3','\nb4','\nb5','\nb6']
with open("Documents/code/udemy/python-for-beginners/python-for-beginners/ids.txt", 'w') as file:
    for id in ids:
        file.write(id)

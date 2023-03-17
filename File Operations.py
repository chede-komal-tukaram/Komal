#File Reading Operations
# go to file path  or folder and locate file with file name
#open file
#Read content/write content to file.
# copy content you got from file and use it file close

# filevariable = open(r"D:\Komal\sample.txt")     # r is for row string
# filevariable = open("sample.txt")
# content = filevariable.read()
# print("file content : ",content)
# filevariable.close()


##=============================================================================================

# try :
#     filevariable = open(r"D:\Komal\sample.txt")
#     filevariable = open("sample.txt")
#     content = filevariable.read()
#     print("Something went wrong")
# finally:
#     filevariable.close()            #Something went wrong

#====================================================================================================

# try:
#     filevariable = open(r"D:\Komal\sample.txt")
#     filevariable = open("sample.txt")
#     content = filevariable.read()
#     print("file content :",filevariable.read())
# except:
#     print(("something went wrong"))
# finally:
#     try:
#         filevariable.close()
#     except:
#         print("File never opened...")               #file content : 
# #----------------------------------------------------------------------------------------------
### another way to open file

# with
open (r"D:komal\sample.txt",'r') as filevariable:
filecontent = filevariable.read()
print(filecontent)

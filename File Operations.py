#File Reading Operations
#go to file path  or folder and locate file with file name
#open file
#Read content/write content to file.
#copy content you got from file and use it file close

# filevariable = open(r"D:\Komal\sample.txt")     # r is for row string
# filevariable = open("sample.txt")
# #if you don't provide full path then it use relative path # search in same folder where you have program
# content = filevariable.read()
# print("file content : ",content)
# filevariable.close()              #file content :  we are now expert in python....


#=============================================================================================

# try :
#     filevariable = open(r"D:\Komal\sample.txt")
#     filevariable = open("sample.txt")
#     content = filevariable.read()
#     print("Something went wrong")
# finally:
#     filevariable.close()            #Something went wrong

# #====================================================================================================

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
# # #----------------------------------------------------------------------------------------------
# ### another way to open file for read mode

# with open (r"D:\Komal\sample.txt",'r') as filevariable:
#     filecontent = filevariable.read()
# print(filecontent)
# ## file will automaticcaly closed with or without exception

# ##================================================================================================
# 3# file writing operation

# # # go to file path and locate file with filw name
# # # open file name
# # # write content in file
# # # save file if you made changes (only when you made write something in file)
# # # file close


# with open(r"D:\Komal\sample.txt",'w') as filevariable:
#         filevariable.write("we are now expert in python....")
#         print("file writing is compleated")             #file writing is compleated

#file will automatically closed with or without exception

# ##=========================================================================================================
# with open (r"D:\Komal\sample.txt",'r+') as filevariable:
#         filevariable .write("we are now expert in python...")
#         print("file writing is compleated....")     #file writing is compleated....


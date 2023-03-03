#  Indexing is always start with 0  index
# which index is not present in the string it gives error

# string = "kalyani sandip shinde"
# print(string)
# print(len(string))
# strlen = len (string)
# print(strlen)
# print(string[strlen - 1])
      
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])
# print(string[6])
# print(string[2:6])      #2 is starting position      dought here#####


#--------------------------------------------------------------------------------------
# wrong way to do this 
# print(string[0]+string[1]+string[2]+string[3]+string[4]+string[5]+string[6])

#correct way to do this
# string = "kalyani sandip shinde"
# print(string[0:2])
# print(string[0:3])          #kal
# print(string[0:21])
# print(string[::-21])    e
# print(string[:-12])
# print(string[:21])      #kalyani sandip shinde
# print(string[8:14])         #sandip
##------------------------------------------------------------------------------------------------------

# str = "welcome"
# print(str[-7 :-1])      #welcom
# print(str[-1 :-7])      #empty
# print(str[-7 :-1])      #welcom
# print(str[-7 :-1])      
# print(str[:])               #welcome  

##------------------------------------------------------------------------------------------
# avalue = "welcome"
# print(avalue[-7 :-1])     #welcom

# print(avalue[ 0 : 7 :1])      #welcom
# print(avalue[ 0 : 7 :2])      #welcom
# print(avalue[ 0 : 7 :3])      #welcom


#************************************************************************************
#some questions about string slicing
#Q1 Reverse the string?
# str = "reverse me"        # method 1
# print(str[::-1])

# take input from user:
# s = input("Enter a string:")        #method 2
# my_str =s[::-1]
# print(my_str)

#reverse  a string using for loop
# s= input("enter a string :")
# str = ''
# for i in s :
#     str = i + str
#     print ("The reversed string is : " ,str)

#using reverse method
# string ="innovant"
# string =list(string)
# string.reverse()
# print(string)







##--------------------------------------------------------------------------------------------------



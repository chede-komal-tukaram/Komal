# print("hello")
# print("hello world")
# a = [10,4,5,20,90,20]
# print(a[3])
# print(a[4])     #syntax is correct

# # Runtime exception : error or exception is occured even syntax is correct.

# # program will terminate in case of syntax error or runtime exception.
# # ---------------------------------------------------------------------------------------------
# a = [10,4,5,20,90,80]
# try:
#     print(a[3])         #syntax is correct
#     print(a[2])         #syntax is correct
#     print(a[6])         #Indexerror:
#     print(a[0])         #will not execute
#     print(a[-1])        #will not execute
# except:     # except block will execute on runtime exception or syntax error.
#     print("something went wrong")

# print("program is compleated")
# #----------------------------------------------------------------------------------------------------------------

# a = [10,40,50,90,25]

# try:
#     print(a[3])         #syntax is correct
#     print(a[2])         #syntax is correct
#     # print(a[6])         #Indexerror:
#     print(a[0])         #will not execute
#     print(a[-1])        #will not execute
# except:             ## except block will execute on runtime exception or syntax error.
#     print("something went wrong")

# print("program is compleated")
# # --------------------------------------------------------------------------------------------
# a = [10,40,50,90,25]

# try:
#     print(a[3])         #syntax is correct
#     print(a[2])         #syntax is correct
#     print(a[6])         #Indexerror:
#     print(a[0])         #will not execute
#     print(a[-1])        #will not execute
# except Exception as ex:             ## except block will execute on runtime exception or syntax error.
#     print("something went wrong",ex)

# print("program is compleated...")
# # ----------------------------------------------------------------------------------------------------

# # Exception is class, common base class for all exception.

# #-------------------------------------------------------------------------------------------
# a = [10,40,50,90,25]

# try:
#     print(a[3])         #syntax is correct
#     print(a[2])         #syntax is correct
#     print(a[6])         #Indexerror:
#     print(a[0])         #will not execute
#     print(a[-1])        #will not execute
# except Exception as ex:             ## except block will execute on runtime exception or syntax error.
#     print("something went wrong",ex)
# except IndexError as ie:
#     print("Given index not present", ie)

# print("program is compleated...")
# #------------------------------------------------------------------------------------------------

# # only one except will get executed. then sequence is important.
# # if execution is handled in most matching block then another except block will not execute.
# # Exception is parent for all exceptions and capable to handle all type of execution like Indexerror
# # ,Nameerror,etc
# # Hence , we should all the time specify exception block at last.


# try:
#     inputNumber = input("Enter number to divide to 100 : ")

#     result = 100/int(inputNumber)
#     print("Result : ",result)

# except ZeroDivisionError as z : 
#     print("You cannot enter 0 as input : ",z)
# except ValueError as v:
#     print("Input value is invalid ",v)
# except Exception as ex:
#     print("Error occured :",ex)
# ##-----------------------------------------------------------------------------
# try:
#     inputNumber = input("Enter number to divide to 100 : ")
#     result = 100/int(inputNumber)
#     print("Result :",result)
# except ZeroDivisionError as z :
#     print("You can not enter 0 as input :",z)
# except ValueError as v :
#     print("Input value is invalid ",v)
# except Exception as ex:
#     print("Error occured :",ex)                     #Enter number to divide to 100 : 65
#                                                         #Result : 1.5384615384615385
#                                                         #program  compleated successfully.......
# finally:
#     print("program  compleated successfully.......")
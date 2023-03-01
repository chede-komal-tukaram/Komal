#first program in python 
# print ("hello world")
# print ("hello innovant")
# print ("5+5")
# print(5+5)
# print("5 + 5=",5 +5)
# print(3.14)

# #assignment
# #print table of 10
# print (10 * 1)
# print (10 * 2)
# print (10 * 3)
# print (10 * 4)
# print (10 * 5)
# print (10 * 6)
# print (10 * 7)
# print (10 * 8)
# print (10 * 9)
# print (10 * 10)

# num = 10
# print(num *1)
# print(num *2)
# print(num *3)
# print(num *4)
# print(num *5)
# print(num *6)
# print(num *7)
# print(num *8)
# print(num *9)
# print(num *10)

##------------------------------------------------------------------------------
#from math import pi
#print(pi)

# a = 10
# print(10)
# print(a)

# a = 20 
# print(10)
# print(a)

# a = 40
# print(10)
# print(a)

# a = 10  integer
# a2= -20 integer
# b= 12.3 Floating
# b2 = -12.3 Floating
# c = '10'    String 
# c2 = "hello" string 
# c3 = '''hello''' string 
# d = True 
# print (True)
# d2 = False
# print(False)
# e = none
# print(none)

# a = 10
# print(a)
# temptype = type(a)
# print(temptype)
# print(type(a))

# b = 16.5
# print(b)
# print(type(b))

# c2 = "hello"
# print(type(c2))

# c = '''something'''
# print(type(c))

# d2= False
# #print(d)
# print(type(d2))

#temp = 1
#print(type(temp))

#---------------------------------------------------------------------------------------------
#10 + 10 = 20
# print(10+10)
# print("10+10")
# print(10 +"10")

# avalue = 10
# bvalue = "20"
# print(str(avalue)+bvalue)

# print(int("10"))
# print(int("10sss"))


#print (int(float("13.3")))

# avalue = "komal"
# print (type(bool(avalue)))
# print(bool(avalue))

# avalue = ""
# print(type(eval(avalue)))
# print(eval(avalue))

#3---------------------------------------------------------------------------------------

# avalue = "welcome"
# #print (f"length of avalue : {len(avalue)}")
# #print(f"{len(avalue)}")

# result = avalue.startswith('w')
# print(f"{avalue} startswith('w':{result}")


# avalue = "welcome"
# result = avalue.endswith('Come')
# print (f"{avalue} startwith'Come':{result}")


#avalue = "welcome"
# result = avalue.capitalize()
# print(f"{avalue} capitalize():{result}")


# avalue ="welcome"
# result = avalue.upper()
# print(f"{avalue}upper:{result}")

# result = avalue.lower()
# print(f"{avalue} lower : {result}")

# avalue = "welcome"
# result = avalue.find('co', 2,5)
# print (f"index of 'co' in {avalue}:{result}")


# avalue = "welcome"
# result = avalue.find('e',1)
# print(f"Index of 'e' in {avalue}:{result}")


# avalue = "welcome"
# result = avalue.replace('come','done')
# print(f"replace 'come'with 'done' in {avalue} : {result}")

# result =avalue.replace('come','done').replace('done','played').upper() 
# print (f"replace 'come' with 'done' in {avalue} : {result}")

# string slicing

# avalue ="welcome"
# print (avalue)
# print(avalue[0])
# print(avalue[1])
# print(avalue[2])
# print(avalue[3])
# print(avalue[7])

#inputvalue =input("enter string")
# avalue = "welcome"
# strlen = len(avalue)
# print(avalue[strlen-1])

# print (avalue [0:2])
# print(avalue[3:6])
# print (avalue[3:8])

# avalue = "welcome"
# print(avalue[-1:0])

# a = 10 
# print(a,type(a))

# colors = ['red','green','blue','black','pink']
# print(colors,type (colors))


# avalue = "welcome"
# avalue[0]
# print(colors[4])

# print(colors)

#---------------------------------------------------------------------------------------
# sampledictionary = {'key' :'value',1001 :'pune'}

# empdictionary = {
#                     101 :[101,'priya','98855'],
#                     102 :[102,'manoj','78965'],
#                     103 :[103,'saurabh','65432'],
#                     104 :[104,'savan','987654'],
#                     105 :[105,'komal','98765'],
#                     106 :[106,'namrata','678905']
#                     }

# print (empdictionary[103])          #[103, 'saurabh', '65432']
# print (empdictionary[105])              #[105, 'komal', '98765']      

# if given key is not present in dictionary,will result in error
# print (empdictionary[0])               #keyerror:0


# empdictionary = {
#                     'pari' :[101,'pari','98855'],
#                     'manoj' :[102,'manoj','78965'],
#                     'saurabh' :[103,'saurabh','65432'],
#                     'savan' :[104,'savan','987654'],
#                     'komal' :[105,'komal','98765'],
#                     'namrata' :[106,'namrata','678905'],
#                     'manoj':[108,'manoj','98654']
#                     }

# print (empdictionary['manoj'])          #[108, 'manoj', '98654']

# print (empdictionary['Manoj'])          # keyerror ; manoj  (capital M)
# #dictionary is mutable ## value assignment is possible
# empdictionary['manoj']= [108,'manoj','2222222']
# print(empdictionary['manoj'])       #[108, 'manoj', '2222222']

# empdictionary['manoj'] = [109,'manik','33333']
# print (empdictionary['manoj'])

# print (empdictionary['manoj'][2])

# empdictionary['manoj'][2]='9999999'
# print(empdictionary['manoj'])

# --------------------------------------------------------------------------------------------
# atemp = {
#             'id' :1001,
#             'favcolor' :'white',
#             'institute':'innovant',
#             1 :'monika',
#             True : "india"
#         }
# print(atemp['favcolor'])    # white
# print (atemp['newkey'])     # keyerror:newkey

# print (atemp.get('favcolor'))       # white

# #if key not present then none..no error
# print (atemp.get('newkey')) 
# print(atemp[1])    #none
# ##-------------------------------------------------------------------------------------------


#loop statement
# alist = [10,35,23,54,87,55,22]
# for item in alist :
#     print(item,end = ' - ')


# alist = [10,35,23,54,87,55,22]
# for item in alist :
#     print(item,end = ' ')

# alist = [10,35,23,54,87,55,22]
# for item in alist :
#     print(item,end = '\n')

# list = [10,35,23,54,87,55,22]
# for item in list:
#     if item ==23:
#         break
#     print(item)

# list = [10,35,23,54,87,55,22]
# for item in list:
#     if item ==23:
#         continue
#     print(item)


# list = [1,2,3,4,5,6,8]
# for item in list:
#     if item ==7:
#         pass
#     print(list)


# list = [10,20,30,40,50,60,43,22,11]
# for item in list:
#     if item ==50:
#         pass
#     print(item)
# else:
#     print("loop compleated execution")

##-------------------------------------------------------------------------------------------
# icounter = 0
# while icounter <5:
#     print("hello innovant")
#     icounter = icounter +1

# num = 10
# icounter = 1
# while icounter <=10:
#     print(num * icounter)
# icounter = icounter + 1

##------------------------------------------------------
#alist = [10,20,30,40,50,60,70,80]
# print(alist[0])
# print(alist[1])
# print(alist[2])
# print(alist[3])

# icounter = 0 
# while icounter <=6:
#     icounter<=len(alist) - 1
#     print(alist[icounter])
#     icounter = icounter +1

# icounter = 0 
# while icounter <=6:
#     icounter <=len(alist)-1
#     if alist [icounter]==60 or alist[icounter]==80:
#         print(alist[icounter])
#         icounter = icounter + 1



###==========================================================================================

# print(aList[0])
# print(aList[1])
# print(aList[2])
# print(aList[3])
# print(aList[4])
# print(aList[5])

# iCounter = 0
# while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
#     print(aList[iCounter])
#     iCounter = iCounter + 1 


# alist = [10, 43, 90, 67, 60, 35, 45]
# iCounter = 0
# while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
#     if aList[iCounter] != 60 and aList[iCounter] != 90:
#         print(aList[iCounter])
#     iCounter = iCounter + 1 

#------------------------------------------------------------
# aList = [10, 43, 90, 67, 60,35,45]

# iCounter = 0
# while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
#     if aList[iCounter] != 60 and aList[iCounter] != 90:
#         print(aList[iCounter])
#     iCounter = iCounter + 1 

# alist = [10, 43, 90, 67, 60, 35, 45]
# iCounter = 0
# while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
#     if alist[icounter] != 90 and alist[icounter] != 60:        print(aList[iCounter])
#     iCounter = iCounter + 1 

####-------------------------------------------------------------------------------------------

'''for loop'''
#alist = [10, 43, 90, 67, 60, 35, 45]
# for item in alist:
#     print(item)

# for item in alist:
#     if item % 2 != 0:
#         print(item)   

# for item in alist:
#     if item % 2 ==0:
#         print("even number is :",item)
#     else:
#         print("odd number is : ", item)        

#for index in range (10,20,2):
 #           print(index)

# alist = [11,64,76,98,45,43,12,23,34,45,56]

# for item in alist:
#     if item % 2 ==0:
#         print("even number : ",item)
#     else:
#         print("odd number :",item)

##=============================================================
'''conditional expeassion'''
# a = 20
# if (a == 10):
#     print("equals")
# else:
#     print("not equals")

# a = 10
# if a >10:
#     print("greater")
# if a>= 10:
#     print("greater or equals")  
# if a < 10 :
#     print("lesser")
# if a <=10:
#     print("lesser or equals")  
# if a == 10:
#     print("equals")
# else:
#     print("god knows")

##--------------------------------------------------------------------------------
# a = 9
# if a > 10:
#     print("greater")
# elif a >=10:
#     print("greater or equal")
# elif a == 10:
#     print("equals")
# else:
#     print("god knows")

# #------------------------------------------------------------------------

# a = 10
# else : (a != 10)
#         print("equals")

# a = 10 
# if: (a != 10):
#     print("equals")



##-----------------------------------------------------------------------------------------------
#'''input function'''
# a = 10
# b = 20
# result = a + b
# print(result)

# a = input("enter first value : ")
# b = input ("enter second number: ")
# result = a + b
# # print(result)

##-------------------------------------------------------------------
# '''factorial of number'''
# #factorial of 10

# counter = 10
# result = 1
# while counter > 1:
#     result = result * counter
#     counter = counter - 1
# print ("factorial of number 10 : ",result)


##---------------------------------------------------------------------
'''operators'''
#arithmatic operator

# print (10 + 5)
# a = 10 
# b = 20
# print("a < b",a <b)



# a = 10
# b = 20
# print("a>=10 and b <= 20",a>=10 and b>= 20)

# # a = 10
# b = 20
# print("a>10 or b < 20",a>10 or b> 20)

# a = True
# b = False
# print("a not", not a )
# print("b not", not b)



#-------------------------------------------------------------------------
'''custom functions'''




##----------------------------------------------------
'''exception'''
#print("hello")
##Print("Hello world") ## syntax error   #NameError: name 'Print' is not defined

# program will terminate on syntax error

# a = [10, 4, 5,20, 89]
# print(a[3])
# print(a[3])## syntax is corrent
#print(a[5])    ## syntax is corrent  #IndexError: list index out of range

# # # Runtime exception : error or exception is occurred even though syntax is correct

# # program will terminate in case of syntax error or runtime excpetion
# ##------------------------------------------------------------------------
# a = [10, 4, 5,20, 89]
# try:
#     print(a[3])
#     print(a[2])## syntax is corrent
#     print(a[5])    ## syntax is corrent  #IndexError: list index out of range
#     print(a[0])   ## will not execute
#     print(a[-1])   ## will not execute
# except: ## except block will execute on runtime exception or syntax error
#     print("Something went wrong")

# print("program is completed...")
##------------------------------------------------------------------------
# ##------------------------------------------------------------------------
#a = [10, 4, 5,20, 89]
# try:
#     print(a[3])
#     print(a[2])## syntax is corrent
#     print(a[5])    ## syntax is corrent  #IndexError: list index out of range
#     print(a[0])   ## will not execute
#     print(a[-1])   ## will not execute
# except: ## except block will execute on runtime exception or syntax error
#     print("Something is wrong")

# print("program is completed...")
# #------------------------------------------------------------------------
# ##------------------------------------------------------------------------
# a = [10, 4, 5,20, 89]
# try:
#     print(a[3])
#     print(a[2])## syntax is corrent
#     print(a[5])    ## syntax is corrent  #IndexError: list index out of range
#     print(a[0])   ## will not execute
#     print(a[-1])   ## will not execute
# except Exception as ex: ## except block will execute on runtime exception or syntax error
#     print("Something went wrong", ex)

# print("program is completed...")
##------------------------------------------------------------------------

# #Exception is class, Common base class for all exceptions.

# #------------------------------------------------------------------------
# a = [10, 4, 5,20, 89]
# try:
#     print(a[3])
#     print(a[2])## syntax is corrent
#     print(a[5])    ## syntax is corrent  #IndexError: list index out of range
#     print(a[0])   ## will not execute
#     print(a[-1])   ## will not execute
# except Exception as ex: ## except block will execute on runtime exception or syntax error
#     print("Something went wrong", ex)
# except IndexError as ie:
#     print("Given index not present", ie)


# print("program is completed...")
# #------------------------------------------------------------------------
# # Only one except will get executed.. then sequence is important
# # if exception is handled in most matching block then another except block will not execute
# #Exception is parent for all exceptions and capable to handle all type of excetions like IndexError, NameError, etc
# # Hence we should all the time specify Exception block at last


# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
    
#     result = 100 / int(inputNumber)
#     print("Result : ", result)

# except ZeroDivisionError as z: ##(Sorry, Dubara nahi karenge, if this excepttion doesnt match then next one will be checked)
#     print("YOu can not enter 0 as input: ",z)
# except ValueError as v:
#     print("Input value is invalid ", v)
# except Exception as ex:       ##(chappal)
#     print("Error Occured : ", ex)





###==============================================================================

#

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
    
#     result = 100 / int(inputNumber)
#     print("Result : ", result)

# except ZeroDivisionError as z: ##(Sorry, Dubara nahi karenge, if this excepttion doesnt match then next one will be checked)
#     print("YOu can not enter 0 as input: ",z)
# except ValueError as v:
#     print("Input value is invalid ", v)
# except Exception as ex:       ##(chappal)
#     print("Error Occured : ", ex)
# finally:        # you can write any code which you wish to execute in exception or without exception
#     print("Program completed successfully...")  ## I execute all the time

#-------------------------------------------------------------------------
'''file operation'''

##-------------------------------------------------------------------
'''functions'''

##-----------------------------------------------------------
'''use function of outside file'''
#import CustomFunctions      ## importing user defined module
# import os                   ## importing inbuilt module
# import math                 ## importing inbuilt module
# import playsound            ## importing external module

# result = CustomFunctions.isAdult(26)
# print(result)   #True

# result = CustomFunctions.isAdultInString(26)
# print(result)   #Adult
# ##------------------------------------------------------
'''class and object'''

##--------------------------------------------------------
'''class with multiple object'''

##--------------------------------------------
'''init constructor'''

# class BillingCustomer:
#     billId = 000
#     address = 'pune'
#     billAmount = 0 

#     def getBillingDetails(self):
#         return f" Bill ID : {self.billId},address : {self.address},bill Amount :{self.billAmount}"
# billobj = BillingCustomer()
# billInfo =billobj.getBillingDetails()
# print(billInfo)
##==----------------------------------------------------------------------------------------------------
#constructor
# class BillingCustomer:
#     billId = 000
#     address = 'karmala'
#     billAmount = 0
#     def __init__(self):
#         print("i am constructor of BillingCustomer")

#     def getBillingDetails(self):
#         return f"Bill ID :{self.billId},address :{self.address},billAmount : {self.billAmount}"
# billobj = BillingCustomer()
# billobj.billId =111
# billobj.billAmount = 100
# billInfo = billobj.getBillingDetails()

# print(billInfo)

# billobj2 = BillingCustomer()
# billobj2.billId = 111
# billobj2.billAmount = 100
# billInfo = billobj.getBillingDetails()
# print(billInfo)
##------------------------------------------------------------------------------------------------
# ##constructors
# class BillingCustomer:
#     billId = 111
#     address ='pune'
#     billAmount =100

#     def __init__(self):
#     self.billId =222
#     self.billAmount =200
#     self.isCorrectionRequired= False
# print("I am constructor of BillingCustomer")
#         def


##===========================================================================================
'''constructor'''

# class BillingCustomer:
#     billId = 000
#     address = 'osmanabad'
#     billAmount = 0
#     def getBillingDetails(self):
#         return f"Bill ID :{self.billId},Address :{self.address}, billamount :{self.billAmount}"
# billobj = BillingCustomer()
# billInfo = billobj.getBillingDetails()
# print(billInfo)
##------------------------------------------------------------------------------------------------------
'''CONSTRUCTOR
'''
# class BillingCustomer:
#     billId = 111
#     address = 'ahemadnagar'
#     billAmount = 100

#     def __init__(self):
#         print("I am constructor of BillingCustomer")

#     def getBillingDetails(self):
#         return f" billid : {self.billId},address : {self.address},billAmount : {self.billAmount}"
    
# billobj = BillingCustomer()
# billobj.billId = 222
# billobj.billAmount = 200
# billInfo = billobj.getBillingDetails()
# print(billInfo)


# billobj2 = BillingCustomer()
# billobj2.billId = 222
# billobj2.billAmount = 200
# billInfo = billobj.getBillingDetails()
# print(billInfo)

#-----------------------------------------------------------------------------------------------------------
# class BilingCustomer:
#     billId =000
#     address ="pune"
#     billAmount =000

#     def __init__(self):
#         self.billId =555
#         self.billAmount = 0000
#         self.isCorrectionRequired =False
#         print("Iam shinde komal sandip")

# def getBillingDetails(self):
#     return f"Bill ID : {self.billId},address : {self.address},bill amount :{self.billAmount}"

# billobj=BillingCustomer()
# billInfo = billobj.getBillingDetails()

# print(billInfo)

# billobj2 =BillingCustomer()
# billInfo = billobj2.getBillingCustomer()
# print(billInfo)

# billobj.__init__()
# billobj2.__init__()




# class BillingCustomer:
#     billId = 000        # class attribute
#     address = 'Pune'    # class attribute
#     billAmount = 0      # class attribute

#     #Automatically get execute when new object getting created and same object will be passed as arguement to self
#     # init(self) having only one parameter which is self is a default constructor
#     def __init__(self) -> None:     #self : a class object which is being created
#         self.billId = 111                       # Object attribute
#         self.billAmount = 100                   # Object attribute
#         self.isCorrectionRequired = False       # Object attribute
#         print("I am constructor of BillingCustomer")

#     def getBillingDetails(self):        # method
#         return f"Bill ID : {self.billId}, Address :  {self.address}, Bill Amount : {self.billAmount}"

# billObj = BillingCustomer()         ## Object creation
# billInfo = billObj.getBillingDetails()      # method call by using object
# print(billInfo)     #Bill ID : 111, Address :  Pune, Bill Amount : 100

# billObj2 = BillingCustomer()         ## Object creation
# billInfo = billObj2.getBillingDetails()      # method call by using object
# print(billInfo)     #Bill ID : 111, Address :  Pune, Bill Amount : 100

# billObj.__init__()     ## Manual way to call cunstructor
# billObj2.__init__()     ## Manual way to call cunstructor


##=======================================================
# '''class and object'''
# empid = 1001
# name = 'komal'
# address = 'pune'
# salary = '100000'

# def getEmployeeDetails():
#     print(f"Emp id = {empid},name : {name},address: {address},salary :{salary}")
# getEmployeeDetails()

# ##--------------------------------------------------------------------------------
# '''class creation'''
# class Employee:
#     empid = 1001
#     name = 'komal'
#     address = 'karmala'
#     salary = '50000'

#     def getCompany():
#         print("innovant")
#         Employee.getCompany()
#         print(Employee.salary)

# ##---------------------------------------------------------------------------
# '''object creation'''
# emp = Employee()
# Employee.getEmployeeDetails(emp)
# Employee.getCompany()

##------------------------------------------------------------------
'''class with multiple object '''
# class Employee:
#     empid = 1001
#     name = 'komal'
#     address = 'pune'
#     salary = '50000'
    
#     def getInfo(self):
#         print (f"emp id ={self.empid},name : {self.name},address:{self.address},salary:{self.salary}")

#     def updateInfo(selfie,empid,name,company):
#         selfie.empid = empid
#         selfie.name = name
#         selfie.company = company

# emp = Employee()
# emp2 = Employee()
# emp.getInfo()
# emp2.getInfo()
# Employee.updateInfo(emp,2002,"kalyani","IBM")

# emp.getInfo()
# emp2.getInfo()

# print(emp.company)
# print(emp2.company)

##--------------------------------------------------------------------------
'''USE THE FUNCTION OUTSIDE FILE'''
# import CustomFunctions

# #import math

# result = CustomFunctions.isAdult(26)
# print(result)

# result = CustomFunctions.isAdultInstring(26)
# print (result)


##---------------------------------------------------------------------------
'''INPUT FUNCTIONS'''

# a = 10
# b = 20
# result = a +b
# print(result)

# a = input("Enter first number :")
# b = input("Enter second number :")
# result = a +b 
# print(result)




# a = 10 
# b = 20
# result = a + b
# print(result)

# #=============================================
# ## input function always accept input values as string 

# a = input("Enter first number : ") 
# b = input("Enter second number: ") 
# result = a + b
# print(result)

# #--------------------------------------------

# a = input("Enter first number : ") 
# b = input("Enter second number: ") 
# result = int(a) + int(b)    ### typecasting
# print(result)
# ##--------------------------------------------

# a = int(input("Enter first number : ")) ### typecasting
# b = int(input("Enter second number: ")) ### typecasting
# result = a + b    
# print(result)
# ##--------------------------------------------
# a = int(input("Enter first number : ")) ### typecasting
# b = int(input("Enter second number: ")) ### typecasting
# print(int(a) + int(b) )

# ##--------------------------------------------
# print(int(input("Enter first number : ")) + int(input("Enter second number: ")))

# print("hi")
# print("hello innovant")
# print('hello world')


#=============================================================================


#class and object :
#create  class:-
# empid = 1001        #attribute
# name = 'savan'      #variable
# address ='pune'    #variable
# salary ='100000'    #variable

# def getEmployeeDetails():       #function defination #user defined
#     print(f"Emp id :{empid},Name :{name},Address :{address},salary :{salary}")      #function body

# getEmployeeDetails()    #function call
#     ##======================================================================================
# #class creation 
# class Employee:
#  empid = 1001
#  name = 'savan'
#  address = 'pune'
#  salary = '100000'

#  def getEmployeeDetails(self):
#         print(f"Empid = {self.empid},Name :{self.name},address :{self.address},salary : {self.salary}")

#  def getCompany():
#         print("innovant")

# Employee.getCompany()
# # Employee.getEmployeeDetails()

# print(Employee.salary)





# empid = 1001            #variable  # int
# name = 'Savan'          #variable   # str
# address = 'Pune'          #variable
# salary = '9000000'          #variable

# def getEmployeeDetails():       # function defination  # user defined
#     print(f"Emp id = {empid}, Name : {name}, address : {address}, salary : {salary}")       # function body

# getEmployeeDetails()        ## function call

# ###=============================================================================
# ## class creation
# class Employee:         # class => keyword to define class , Employee => class name, it can be anything and first char of each word has to be capital
#     empid = 1001            #attribute  # int
#     name = 'Savan'          #attribute   # str
#     address = 'Pune'          #attribute
#     salary = '9000000'          #attribute

#     def getEmployeeDetails(self):       # method defination  # user defined
#         print(f"Emp id = {self.empid}, Name : {self.name}, address : {self.address}, salary : {self.salary}")       # function body

#     def getCompany():       # self need to pass only when we need to use class attribute
#         print("Innovant")

# Employee.getCompany()           #Innovant ## way to call class method
# ###Employee.getEmployeeDetails()       ## missing 1 required positional argument: 'self'
# print(Employee.salary)      #9000000

# ## self : is a first parameter to method if you want to access class attribute
# ## self : it is not mandatory to have name as self, it can be anything like selfie or anything
# ## parameter : when you define function then parameter
# ## argument  : when you call function then you are providing values, that time argument



##========================================================================================

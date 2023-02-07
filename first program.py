# print ("hello world")
# print ("hello coders")
# print("i know how to count.....1234")
# ##-------------------------------------------------------------------------------------------------
# name =("komal")
# age = 23
# print(name)
# print(age)
# name= ("kanchan")
# age = 24.0
# print (name)
# print(age)
# is_adult = True
# print(age)

#--------------------------------------------------------------------------------------------------
#take input from user
#name = input("what is your name?")
#print("hello" +name)
#==-------------------------------------------------------------------------------------------
#type conversion:

#old_age = input("enter your old age :")
#new_age =int(old_age)+2
#print (new_age)
#---------------------------------------------------------------------------------------
# first = input ("enter first number :")
# second = input ("enter second number :")
# sum = int(first) + int(second)
# print (sum)
##-----------------------------------------------------------
#name ="tony stark"
# print (name.upper())
# print (name.lower())

# print(name.find('stark'))

#print (name.replace("t","m"))
#print(name)
##================================================
#name = "tony stark"
#print("m" in name)
##-----------------------------------------------------------------------------------------
#arithmatic operator:
# print(5+2)
# print (4-3)
# print (4*3)
# print (4//3)
# print (5%2)
# print (5**2)

#================================
# i = 5 
# i = i +2
# i +=2
# i -=2
# i *=2
# result = 2+3*5 
# print (result)

# result = 2+3/5 
# print (result)
#3------------------------------------------------------------------------------------------
# print(3<=2)
# print(3>=2)
# print(3!=2)

# print(2<3 and 2>1)
# print(not 3<2)

#---------------------------------------------
# age = 3 
# if age >=18:
#     print ("you are an adult")
#     print("you can vote")
# elif age<18 and age >3:
#     print ("you are in school")
# else :
#     print("you are a child")



# first = input ("enter first number : ")
# operator = input("enter operator(+,-,/,*):")
# second = input("enter second number :")


# first = int(first)
# second = int(second)
# if operator =="+":
#     print (first +second) 
# elif operator =="-":
#     print (first +second) 
# elif operator =="/":
#     print (first +second) 
# elif operator =="*":
#     print (first +second) 
# elif operator =="%":
#     print (first +second) 
# else:
#     print ("invalied operation")



#print ("hi komal")



##==============================================================================
#conditional expression
# a = 20
# if (a ==10):
#     print("equals")
# else:
#     print("not equals")


# a = 10
# if a>10:
#     print("greater")
# elif a >=10:
#    print("greater or equal")
# elif a <= 10:
#     print("lesser or equals")
# elif a == 10:
#     print ("equals")
# else:
#     print("god knows")


#class and object 

empid = 1001
name = 'komal'
address = 'pune'
salary = '2000000'

def getEmployeeDetails():
    print(f"Emp id ={empid},name :{name},address:{address},salary :{salary}")
getEmployeeDetails()

# #-----------------------------------------------------------------------------------------------------------
#class creation:
# lass Employee:
#     empid = 1001
#     name = 'komal'
#     address = 'pune'
#     salary = '2000000'

#         def getEmployeeDetails(self):
#                 print(f"Emp id = {self.Empid},name = {self.name},address = {self.address},salary = {self.salary}")

#         def cgetCompany():
#                 Employee.getEmployeeDetails()
#                 print(employee.salary)

#---------------------------------------------------------------------------------------

# class Employee:
#         Empid = 1001
#         name = 'komal'
#         address = 'pune'
#         salary = '2000000'

#         def getEmployeeDetails(self):
#                 print(f"Emp id = {self.Empid},name = {self.name},address = {self.address},salary = {self.salary}")

#         def getCompany():
#                 print("innovant")

#                 Employee.getEmployeeDetails()
#                 print(employee.salary)
# #-------------------------------------------------------------------------------------------------------
# ##object creation:
# #first approtch to call class method by using class object.
# emp =Employee()
# Employee.getEmployeeDetails(emp)
# Employee.getCompany()

# ##----------------------------------------------------------------------------------------------------
# #SECOND APPROTCH TO CALL CLASS METHOD BY USING CLASS OBJECT.
# emp = Employee()
# #emp.getEmployeeDetails(emp)
# emp.getEmployeeDetails()

# #=====================================================================================================

#class creation
# class Employee :
    
#         empid = 1001
#         name = 'komal'
#         address = 'pune'
#         salary = '2000000'
#         company = 'IBM'

#         def getInfo(self):
#                 print (f"Emp id ={self.empid},name :{self.name},address:{self.address},salary:{self.salary}")

#         def updateInfo(selfie,empid,name,company):
#                 selfie.empid = empid
#                 selfie.name = name
#                 selfie.company = company

# emp = Employee()
# emp2 = Employee()
# emp.getInfo()
# emp2.getInfo()
# Employee.updateInfo(emp,2002,"priya","IBM")

# emp.getInfo()
# emp2.getInfo()

# print(emp.company)
# #print(emp2.company)
# ##===============================================================================================
    
# class Employee:         # class => keyword to define class , Employee => class name, it can be anything and first char of each word has to be capital
#     empid = 1001            #attribute  # int
#     name = 'Savan'          #attribute   # str
#     address = 'Pune'          #attribute
#     salary = '9000000'          #attribute

#     def getInfo(self):       # method defination  # user defined
#         print(f"Emp id = {self.empid}, Name : {self.name}, address : {self.address}, salary : {self.salary}")       # function body

#     def updateInfo(selfie, empid, name, company) :       # self is object , empid is parameter, self.empid is referece to self attribute
#         selfie.empid = empid
#         selfie.name = name
#         selfie.company = company        # newly added attribute to only emp object


# emp = Employee()
# emp2 = Employee()
# emp.getInfo()   #Emp id = 1001, Name : Savan, address : Pune, salary : 9000000
# emp2.getInfo()
# Employee.updateInfo(emp, 2002, "Priya", "IBM")      ## selfie = emp, empid = 2002

# emp.getInfo()
# emp2.getInfo()

# print(emp.company)      #IBM
# #print(emp2.company)     #Employee' object has no attribute 'company'
#--------------------------------------------------------------------------------------
#empid = 1001            #variable  # int
# name = 'Savan'          #variable   # str
# address = 'Pune'          #variable
# salary = '9000000'          #variable

# def getEmployeeDetails():       # function defination  # user defined
#     print(f"Emp id = {empid}, Name : {name}, address : {address}, salary : {salary}")       # function body

# getEmployeeDetails()        ## function call

###=============================================================================
## class creation
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

# ##===========================================================================
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

# ##======================================================================

# ## Object creation
# ##-----------------------------------------------
# #first approach to call class method by usning class name
# emp = Employee()        # Employee is class and emp is object,, emp is just object name, it can be anythin
# Employee.getEmployeeDetails(emp)        # we are passing emp object of Employee type to method as self argument 
# Employee.getCompany()        # Innovant
# #-----------------------------------------------------------
# ## second approach to call class method by usnign class object
# emp = Employee()        # Employee is class and emp is object,, emp is just object name, it can be anythin
# ##emp.getEmployeeDetails(emp) #takes 1 positional argument but 2 were given
# emp.getEmployeeDetails() #takes 1 positional argument but 2 were given


###=============================================================================================





print("Kolal")
#lecture no. 1#
#print ("hello")             # hello

#option 1:- python  INT01/firstprogram.py
# option 2:-
            #cd INT01
            #python firstprogram. py
# if you want step out of folder use "cd.."
#if you want in to folder use "cd foldername"

##====================================================================================================
# create file in python
#print ("hello")         # hello
#print ("5+4")           #5+4
#print (5 + 4)           #9
#print (3.14)            # 3.14

##===================================================================================================
# commment file in python
#(#) is used for the single line comment.
#ctrl + / is used for multiple line.

#comment/uncomment:-
#ctrl + k + c  = comment single line comment
#ctrl + k + u = multiple line uncomment


#developed by : Innovant batch 1
#date : 11- jan -2023
#purpose :just first program

# multiple line comment
''' developed by : Innovant batch 1
date : 11-jan-2023
purpose :just first program'''


"""developed by : Innovant batch 1
date : 11-jan-2023
purpose :just first program"""

##*************************************************************************************************

#lecture no. 2
# inbuilt module:-

## inbuilt module comes with python installation
#import math     # impoting or including math library/module
# print ("hello")     # hello
# print (3.14)        # 3.14

# import math
# print (math.pi)         #3.141592653589793

# import os
# print(os.getcwd())

#external module:-
#import selenium # importing externaml module

#pip package manager - to download and install external module.
#pip install- u selenium-comment to install externaml module
#Q.1 you need to play song?

#*******************************************************************************************************
''' variables and datatype in py'''
# print ("hello")
# a = 25          # a is a variable, and 25 is value inside it.
# print (a * 1)
# print (a * 2)
# print (a * 3)
# print (a * 4)
# print (a * 5)
# print (a * 6)
# print (a * 7)
# print (a * 8)
# print (a * 9)
# print (a * 10)      # to print table of 25
#_------------------------------------------------------------------------------------------
# a = 10
# print(10)       #10
# print(a)        #10

# a = 20              #variable value will be changed and further recent value will be used
# print (10)      #10
# print(a)        #20

# a = 40              #variable value will be changed and further recent value will be used
# print (10)          #10
# print (a)           # 40
# ##-===========================================================================================
# #variable are just container to store value of any type

# a = 10      #Integer 
# a2 = -20    #Integer

# b = 15.7    #float type
# b2 = -15.7  # float type

# c = '10'    #string
# c2 = "hello"    #string
# c3 = '''hello,
#             how are you doing today?
#             thank you'''    #string
# print (c3)

# d = True    # boolean type,boolean can contain either true or false
# d2 = False  # boolean type
# d3 = true   # error,coz python is case sensetive and t has to capital in true.

# e = None    # none type , no specific type or unknown.

#================================================================================================
''' types '''
# a = 10          # Integer # 10 is value in variable and it is type of integer so variable will be of same type i.e Integer
# print (a)

# temptype =type(a)           # type will be accept inpit and provide variable type as output
# print (temptype)    #<class 'int'>
# print(type(a))      #<class 'int'>

# #----------------------------------------------------------------------------------------------------
#b = 16.6
#print(type (b))         #<class 'float'>

#--------------------------------------------------------------------------------------------------
#c = "hello"             #  string type
#c2 ='something'         #string type
c3 = '''something
            komal
                shinde'''       # string type
#-----------------------------------------------------------------------------------------------
#d = True        # boolean type,boolean can contain true or false onlt
#d2 = False      # boolean type
#print (d)       # true
#print(type(d))      #<class 'bool'>

#---------------------------------------------------------------------------------------------
#e = None    # none type
#print(type(e))      #<class 'NoneType'>

#interview question:-
#temp = 0
#print(type(0))      #<class 'int'>

#==================================================================================================
'''typecasting'''
#10 + 10 = 20
# print(10 + 10)
# print("10" + "10")      #1010
# print(10 + "10")        #TypeError: unsupported operand type(s) for +: 'int' and 'str'       
#-------------------------------------------------------------------------------------------
# avalue = 10
# bvalue = 20 
# print(avalue + bvalue)      #30
# #----------------------------------------------------------------------------------------------

# avalue = "10"
# bvalue = "20" 
# print(avalue + bvalue)  # 1020
# #---------------------------------------------------------------------------------------------------
# avalue = 10 
# bvalue = "20"
# #print (avalue + bvalue)     #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# #----------------------------------------------------------------------------------------------------
# #int():-take input and create copy and convert in int then provide output
# avalue = 10
# bvalue = "20"
# print (avalue + int(bvalue))        #30
# #--------------------------------------------------------------------------------------
# avalue = 10
# bvalue = "20"
# bvalue = int(bvalue)
# print (avalue + bvalue)     #30
# #--------------------------------------------------------------------------------------
# #str():- take input and create copy and convert str then provide output
# avalue = 10
# bvalue ="20" 
# print(str(avalue) + (bvalue))   #1020
# #----------------------------------------------------------------------------------------------
# avalue = 10
# bvalue = "20"
# avalue = str(avalue)
# print(avalue +bvalue)       #1020
# #-----------------------------------------------------------------------------------------------
# print(int("10"))    #10
# #print (int("10sss"))        #ValueError: invalid literal for int() with base 10: '10sss'
# #print (int("15.5"))         #ValueError: invalid literal for int() with base 10: '15.5'
# print(int (float("15.5")))  #15
# #------------------------------------------------------------------------------------------------
# avalue = "True"
# print (type(bool(avalue)))      #<class 'bool'>
# print (bool(avalue))            #True


# avalue = "False"
# print(type(bool(avalue)))       # bool
# print(bool(avalue))             #true


# avalue = "Innovant"
# print(type(bool(avalue)))       # bool
# print(bool(avalue))             #true

# avalue =""
# print(type(bool(avalue)))       # bool
# print(bool(avalue))             # false
# ## bool function will return all the time true and return false for empty string.

# ##-------------------------------------------------------------------------------------------------
# avalue = "True"
# print(type(eval(avalue)))       #<class 'bool'>
# print (eval(avalue))            # true

# avalue = "False"
# print(type(eval(avalue)))       #<class 'bool'>
# print (eval(avalue))            # false

#avalue = "Innovant"
#print(type(eval(avalue)))       #error
#print (eval(avalue))

# avalue = ""
# print(type(eval(avalue)))       #error
# print (eval(avalue))            # syntaxerror
# in the eval only true and false true other than this syntax error
#-===================================================================================================
'''operators'''
#1. arithmatic operator (+-*/)
#2. assingnment operator(=,+=,-=,*=,/=)
#3.comparison operator(==,>=,<=,<,>,!=)
#4. logical operator(and,or,not)

'''arithmatic operator'''
# print (10+5)        #15
# print(10 - 5)          #5
# print (10 * 5)          #50
# print (10 / 5)          #2.0

# a = 10
# b = 20 
#result = a + b
#print(result)       #30
##--------------------------------------------------------------------------------------------

'''assignment operator'''
# a = 10
# b = 20
# a = a + b # in case of calculation will happen only at right side and will assign value to left side variable
# print ("a =",a,"b =",b)     #a = 30 b = 20


# a = 10 
# b = 20
# a += b           # a = a + b    ## in case of '_'evaluation and calculation will happen only at right side and will assign value to left side variable
# print ("a=",a,"b = ",b)         #a = 30 b = 20

# a = 10
# b = 20
# a -=b           #a = a-b        # in case of '_'evaluation and calculation will happen only at right side and will assign value to left side variable
# print("a = ",a, "b = ",b)       #a =  -10 b =  20



#--------------------------------------------------------------------------------------------------
'''comparison operator'''
# a = 10
# b = 20
# print ("a ==b",a ==b)           #a ==b False

# a = 20
# b = 20 
# print ("a == b",a==b)           #a ==b true

# a = 10 
# b = 20
# print ("a !=b",a!=b)            #a != b true

# a = 20
# b = 20
# print("a != b",a != b)          # a != b false
# ##--------------------------------------------------------------------------------------------------------
# a= 20
# b = 20
# print("a> b",a > b)             # false

# a = 20
# b = 20
# print ("a>=b",a>=b)             #true

# a = 30
# b = 20
# print ("a> b",a>b)          # true

# ##--------------------------------------------------------------------------------------------
# a =20
# b = 20
# print("a<b",a<b)            #false

# a=20
# b = 20
# print ("a <= b",a<= b)      #true

# a = 30
# b = 20
# print ("a<b",a< b)      # false

# a = 30
# b = 20
# print ("a<=b",a <= b)       #a <= b false

##=============================================================================================
'''logical operator'''
#works with boolean
# a = True
# b = True
# print("a and b ", a and b)           #a and b True

# a = True
# b = False
# print("a and b ",a and b)               # a and b faalse

# a = False
# b = False
# print("a and b ",a and b)           # false

# #------------------------------------------------------------------------------------------------
# a = 10
# b = 20
# print ("a > 10 and b < 20",a > 10 and b <20)        # false

# print("a > 10 and b <=20",a > 10 and b <=20)        #a > 10 and b <=20 False

# print ("a>= 10 and b <= 20",a>=10 and b <= 20)                  #a>= 10 and b <= 20 True

# ##-----------------------------------------------------------------------------------------------------
# # or
# a = True 
# b = True
# print ("a or b", a or b)        # a or b true

# a = True
# b = False
# print("a or b ",a or b)         # a or b true

# a = False
# b = False
# print ("a or b ",a or b )       # a or b false
# #------------------------------------------------------------------------------------------
# a = 10
# b = 20
# print("a > 10 or b < 20",a > 10 or b <20)       #false

# print("a > 10 or b <=20",a > 10 or b <= 20)     # true

# print ("a >= 10 or b<= 20",a >=10 or b <=20)            #a >= 10 or b<= 20 True

# ##------------------------------------------------------------------------------------------------

#logical operator always consider any non false value as True
# a = 10          # a will be consider as true
# b = 20          # b will be consider as false

# print("a and b ",a and b)       # a and b 20
# print ("a or b", a or b)        # a or b 10

# #-------------------------------------------------------------------------------------------------------
# a = True 
# b = False
# #print ("a not",a not)       #wrong in syntax
# print("a not",not a)            #a not false
# print("b not",not b)            # b not true


# Q on operators
# write a program here to swap values inside variable
# 1. using max one third variable
# 2. without any third variable
# 3. take input from user and do same 
# a = 30
# b = 20
# ##--------------------------------------------------------------------------------------------------
#=======================================================================================================
"""input function()"""          #remaining
#a = 10 
#b = 20 
# result = a + b
# print (result)      # 30

# # input function always accept input values as string
# a = input("enter first number :")
# b = input("enter second number :") 
# result = a + b 
# print (result)      # 30

# #---------------------------------------------------------------------------------
# a = input ("enter first number :")
# b = input (" enter second number :")
# result = int(a) + int (b)
# print (result)      # 30
# #-----------------------------------------------------------------------------------
# a = int (input ("enter first number :"))
# b = int ( input (" enter second number:"))
# result = a + b
# print (result)

# #-----------------------------------------------------------------------------------------------
#a = int (input("enter first number:"))
#b = int (input ("enter second number :"))
#print (int(a) + int(b))

#------------------------------------------------------------------------------------------------
#print (int(input("enter first number :")))
##=======================================================================================================
"""string slicing"""                        #done

#avalue = "welcome"
#print (avalue)
# indexing will always start with 0 index
# print(avalue[0]) #w
# print (avalue[1]) #e
# print (avalue[2]) #l
# print (avalue[3])   #c
# print (avalue[4])  #o
# print (avalue[5])     #m
# print(avalue[6])    #e
# print (avalue [7])  #IndexError: string index out of range

## last index always be len - 1 
#input value = input ("enter string")
# avalue = "welcome"
# strlen =len(avalue)
# #last index value
# print (avalue[strlen - 1])
# #----------------------------------------------------------------------------------------------------
# ## wrong way to do this..
# print (avalue[0]+avalue[1]+avalue [2])      # wel

# print (avalue[3]+avalue[4]+avalue[5] + avalue[6])       # come
# #------------------------------------------------------------------------------------------------
# avalue = "welcome"
# print(avalue[-1:-7])  # empty string
# print (avalue[-7:-1])   #welcom
# print(avalue[-7:7]) #welcome
# print(avalue[-7:0]) #empty string
# print (avalue[-7:])     #welcome
# print (avalue[:3])      #wel
# print (avalue[:1])      #w
# print (avalue[:])       #welcome
# print(avalue[::-1])     #emoclew
# #------------------------------------------------------------------------------------------------------
# avalue ="welcome"
# print (avalue[0:7])     # welcome
# print(avalue[0:7:1])        #welcome
# print(avalue[0:7:2])        #wloe
# print(avalue[0:7:3])        #wce

##==================================================================================================
"""string functions"""          #remaining

#avalue = "welcome"
#print(f"length of avalue : {len (avalue)}")
#-----------------------------------------------------------------------------------------------------

#avalue = "welcome"
#result = avalue.startswith ('w')
#print ("f {'avalue'} startswith 'w' :{result}")




#===================================================================================================
"""escape character"""



#===================================================================================================
"""list"""
#{}---curly bracket
#()----round bracket
#[]----square bracket

#a = 10
#print (a,type(a))       #10 class integer

# colors = ['red', 'Green','Blue','Black','Pink']

# #print (colors,(type(colors)))       #['red', 'Green', 'Blue', 'Black', 'Pink'] <class 'list'>
# avalue = 'welcome'
# avalue[0]

# print(colors[0])
# print(colors[4])
# print(colors[-1])
# print(colors[3])

# print (colors[0:3])
# #=------------------------------------------------------------------------------------------------------
# colors = ['Red' ,'Green','Blue','Black','Pink']
# newitem = 'white'
# colors[3]= newitem
# colors [4]='yellow'
# print(colors,(type)(colors))

# avalue ='welcome'
# avalue[3]= 'd'   # item assingnment #typeerror ; 'str' object does not suupport item assignment,

#mutable - changable /  we can modify
#immutable - non changeble /cannot modify

#string - immutable # item assignment is not allowment
#list  - mutable # item asignment is allowed

##we can not change single or few element/item/char from string
# however we can replace whole string

# list -we can change single or element/item from list
#also we can replace whole list

#avalue = 'welcome'
#print (avalue)
#avalue = "weldome"
#print (avalue)
##-----------------------------------------------------------------------------------------------------
#avalue ='welcome'
#print (avalue)
#result = avalue.replace('c','d')
#print (result)

# avalue = 'welcome'
# print (avalue[::1])     # welcome
# print(avalue[::-1])     #emoclew
# print(avalue[::2])      #wloe
# print(avalue[::-2])     #eolw
# print(avalue[::-3])     #ecw


# colors = ['Red','Green','Blue','Black','Pink']
# print(colors[::1])          #['Red', 'Green', 'Blue', 'Black', 'Pink']
# print(colors[::-1])         #['Pink', 'Black', 'Blue', 'Green', 'Red']
# print (colors[::2])         #['Red', 'Blue', 'Pink']
# print (colors[::-2])         #['Pink', 'Blue', 'Red']

#=======================================================================================================
"""list operations"""
#colors =['Red','Green','Blue','Black','Pink']
#values =[10,45,2,20,90,66,88]

'''sort'''
# print (len(colors))     #5
# print(f"list before sort{values} ")     #list before sort[10, 45, 2, 20, 90, 66, 88] 
# result = values.sort()
# print(f"list after sort{values}:result :{result}")  #list after sort[2, 10, 20, 45, 66, 88, 90]:result :None


# print (f"list before sort{values}")     #list before sort[2, 10, 20, 45, 66, 88, 90]
# result = values.sort()
# print(f"list after sort{values}:result:{result}")       #list after sort[2, 10, 20, 45, 66, 88, 90]:result:None
# ##--------------------------------------------------------------------------------------------------
'''reverse'''

# values =[10,75,65,35,40,45,50,577,60,100]

# print(len(values))      #10
# print(f"list before reverse{values}")       #list before reverse[10, 75, 65, 35, 40, 45, 50, 577, 60, 100]
# result = values.reverse()
# print(f"list after reverse {values}:result:{result}")       #list after reverse [100, 60, 577, 50, 45, 40, 35, 65, 75, 10]:result:None
# ##-----------------------------------------------------------------------------------------
'''pop'''
#values =[10,75,65,35,40,45,50,577,60,100]

#print (f"list before reverse {values}")     #list before reverse [10, 75, 65, 35, 40, 45, 50, 577, 60, 100]
#result = values.pop(3)     # 3 is index value will be delet from this index deleted value will be in result
#print (f"list after reverse {values}:result:{result}")    #list after reverse [10, 75, 65, 40, 45, 50, 577, 60, 100]:result:35

# print (f"list before reverse {values}")    
# result = values.pop()
# print (f"list after reverse {values}:result:{result}")  #no input means to pop,by default removes last one

#--------------------------------------------------------------------------------------------------
'''remove()'''
#values = [1,2,3,4,5,6,7,8,9,10]

# print(f"list before reverse {values}")  #list before reverse [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = values.remove(5)   # 5 is value or item not index
# print(f"values after reverse {values}:result:{result}") #values after reverse [1, 2, 3, 4, 6, 7, 8, 9, 10]:result:None

# print (f"values before reverse{values}")
# result = values.remove(11)
# print(f"values after reverse{values}:result:{result}")      #value error value is not present in list

#---------------------------------------------------------------------------------------------------------
#values = [10,2,43,9,34,11,45,fds,True]
#values sort() sorting will not work in mix value list


#colors = ['Red','Green','Blue','Black','Pink']
#list is mutable however item inside may be immutable(string)
#print(colors[2][3])

#colors = ['Red','Green',['Blue','Black',['Pink']]]
# print (colors[1][2])
# colors[2][0] = 'new colors'

# print (colors [2][2])       #[pink]
# print (colors[2][2][0])     #pink


##=================================================================================================
"""tuple"""
# avalue = [10,30,50,20,90]
# print (avalue,type (avalue))        # list

# avalue = (10,30,50,20,90)
# print (avalue,type (avalue))        # tuple

# avalue = (10,)          # mandatory is , round bracket is optional.
# print (avalue ,type (avalue))
#--------------------------------------------------------------------------------------------------
#avalue =(10)    # mandatory is , round bracket is optional
#print (avalue,type (avalue))        # class tuple
##----------------------------------------------------------------------------------------------------
#avalue = (10,30,50,20,90)
# print (avalue[1])
# print (avalue[-1])

# tupple is mutable
# avalue [4]=0    #typerror 'tuple object does not support item assignment
# avalue = [10,30,50,20,90]


# avalue .insert (10,2000)        # will work as append if index is out of range
# print (avalue)

##----------------------------------------------------------------------------------------------
##====================================================================================================
"""tuple operations"""
#avalue = (10,30,50,20,90,30,50,10,10)       # tuple
# print (avalue,type(avalue))     # <class 'tuple'>

# print(f"avalue before count(10){avalue}")
# result = avalue.count(10)
# print(f"avalue after count(10){avalue}:result = {result}")      # result = 3
# #---------------------------------------------------------------------------------------------------
#print(f" avalue before count(100){avalue}")
#result = avalue.count(100)
#print (f"avalue after count(100){avalue}:result= {result}")  #result = 0
##----------------------------------------------------------------------------------------------

# list=(10,20,50,80,40,20)
# print(f"list before index(20){list}")
# result = list .index(20)
# print(f"list after index(20){list}:result = {result}") #result =1
# ##---------------------------------------------------------------------------------------------------
# print (f" list before index(20,2){list}")
# result = list.index(20,2)
# print(f"list after index(20,2){list}:result= {result}") # result = 5


#print (f" list before index(40){list}")
#result = list.index(40)
#print(f"list after index(40){list}:result= {result}")# result = 4
#================================================================================================
"""dictionary"""
# employeelist = [
#                 [101,'priya','345678'],
#                 [102,'manoj','98765'],
#                 [103,'saurabh','98765'],
#                 [104,'savan','23456'],
#                 [105,'komal','98766'],
#                 [106,'namrata','8654']
#                 ]


# print (employeelist[2])         #[103, 'saurabh', '98765']

# print (employeelist [0][0]==103)    #false
# print (employeelist [1][0]==103)    #false
# print (employeelist [2][0]==103)    #true
# print (employeelist [3][0]==103)    #false                      ##very lengthy process

###----------------------------------------------------------------------------------------------------
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

#if given key is not present in dictionary,will result in error
#print (empdictionary[0])               #keyerror:0


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

# #print (empdictionary['Manoj'])          # keyerror ; manoj  (capital M)
# ##dictionary is mutable ## value assignment is possible
# empdictionary['manoj']= [108,'manoj','2222222']
# print(empdictionary['manoj'])       #[108, 'manoj', '2222222']

# empdictionary['manoj'] = [109,'manik','33333']
# print (empdictionary['manoj'])

# print (empdictionary['manoj'][2])

# empdictionary['manoj'][2]='9999999'
# print(empdictionary['manoj'])

# #----------------------------------------------------------------------------------------------------
# atempdict = {
#     'id' :1001,
#     '1' : 'manoj'
#     }

# #===============================================================================================
"""dictionary operations"""
# atemp = {
#             'id' :1001,
#             'favcolor' :'white',
#             'institute':'innovant',
#             1 :'monika',
#             True : "india"
#         }

# #print (atemp.items())       #dict_items([('id', 1001), ('favcolor', 'white'), ('institute', 'innovant'), (1, 'india')])
# #dict_items([('id',1001),('favcolor','white'),('institute','innovant'),(1,'india')])

# print (atemp.keys())        #dict_keys(['id', 'favcolor', 'institute', 1])

# atemp ['favcolor']='black'      #exhisting key,value will be overwrite
# atemp ['newkey'] = 'black'      #if new key then it will add to dictionary
# print (atemp)
# #-------------------------------------------------------------------------------------------------------

# atemp = {
#             'id' :1001,
#             'favcolor' :'white',
#             'institute':'innovant',
#             1 :'monika',
#             True : "india"
#         }
# print(atemp['favcolor'])    # white
# #print (atemp['newkey'])     # keyerror:newkey

# print (atemp.get('favcolor'))       # white

# ##if key not present then none..no error
# print (atemp.get('newkey'))     #none
# ###------------------------------------------------------------------------------------------------
# #1 is true and 0 is False
#print (atemp[1])
    #india







##============================================================================================
"""sets"""

# alist =[10,20,80,100,20]        #  duplicated value allowed
# atuple = (10,20,80,100,20)       #duplicated value allowed
# adictionary ={'key':'value',101:'value'}    # duplicate value allowed but key not allowed

# aset = {10,20,80,100,20}        # duplicate value not allowed

# print (aset,type(aset))     #{80, 10, 100, 20} <class 'set'>

# aset = {10,20,40,60,100,20,50}      # duplicate value not allow
# print (aset,type (aset))        #{50, 100, 20, 40, 10, 60} <class 'set'>
# print (len(aset))   #6

#aset = {10,'a',20,80,'y',100,True,80,20, None,10}   # duplicate value not allow
#print(aset)     #{True, 100, 10, 'a', None, 80, 20, 'y'}
                #{True, 100, 'y', 10, None, 'a', 80, 20}
                #{True, 100, 'y', 10, None, 80, 20, 'a'}

#aset = {10,'a',20,80,'y',(100,True,80),20, None,10}
#print(aset)     #{80, 20, 'a', 'y', (100, True, 80), 10, None}          #&&&&OUTPUT CHANGE



#=============================================================================================
"""sets operations"""
# aset = {10,20,30,40,50,20,40,60}
# '''remove'''
# print (f"aset before remove :{aset}")   #aset before remove :{50, 20, 40, 10, 60, 30}
# result = aset.remove(20)
# print(f"aset after remove :{aset} and result :{result}")        #aset after remove :{50, 40, 10, 60, 30} and result :None

##------------------------------------------------------------------------------------------------
'''pop'''
# aset = {10,20,30,40,50,20,40,60}
# print (f"aset before pop :{aset}")      #aset before pop :{50, 20, 40, 10, 60, 30}
# result = aset.pop()
# print(f"aset after pop :{aset}:and result :{result}")       #aset after pop :{20, 40, 10, 60, 30}:and result :50     
# ##------------------------------------------------------------------------------------------------
'''union'''
# aset = {10,20,30,40,50,20,40,60}
# print (f"aset before pop : {aset}")
# result = aset.union({200,10,55})
# print = (f"aset after pop : {aset} and result :{result}")       ##&&&&&7output changed
##-------------------------------------------------------------------------------------------------
# aset = {10,20,80,100,80,20,10}
# print (f"aset before pop :{aset}")      ##aset before pop :{80, 10, 100, 20}
# result = aset.intersection({200,10,55})
# print(f"aset after pop :{aset} and result :{result}")       #aset after pop :{80, 10, 100, 20} and result :{10}


# colors = ["red","black","white","pink",["violet","red"],[[123,345]]]
# print (colors[5])   #[[123, 345]]
# print (colors[-1])  #[[123, 345]]
# print (colors[3])       #pink

##==========================================================================================
"""conditional expression"""
#a = 10 
#if (a == 10):
    #print ("equals")
#else:
    #print("not equals")     # equals
#------------------------------------------------------------------------------

# a = 10 
# if a >10:
#     print ("greater")
# if a >= 10:
#     print ("greater or equal")
# if a < 10:
#     print ("lesser")
# if a <= 10:
#     print ("lesser or equals")
# if a == 10:
#     print ("equals")
# else:
#     print ("god knows")         # greater or equal,lesser or equals ,equals
##-------------------------------------------------------------------------------------------------
# a = 10
# if a >10:
#     print("greater")
# elif a >= 10:
#     print ("greater or equals")
# elif a < 10:
#     print("lesser or equals")
# elif a <= 10:
#     print ("lesser or equal")       # greater or equals
    
##=======================================================================================================
# we can have multiple if statement.
#we can have multiple elif statement.
# we can have only one else statement.

#we have single alone if statement
#we cannot have single alone elif statement
#if we combine if with elif or else we can have only ine if and else 
# however elif can be multiple times

# a = 10 
# if(a != 10):
#     print("equals")

# a = 10 
# else(a != 10):
#     print("equals")

# a = 10 
#     elif(a != 10):
#         print("equals")

##-------------------------------------------------------------------------------------------------
#output will be depend on sequence
# a = 10
# if a > 10:
#     print("greater")
# elif a ==10:
#     print("equals")
# elif a >= 10:
#     print("greater or euals")
# elif a < 10:
#     print ("lesser")
# else:
#     print("god knows")

##-----------------------------------------------------------------------------------------------------------
# a = 30
# if a == 10:
#     print("equals")
# elif a >10:
#     if a >20:
#         print(" supergreater")
# else :
#     print("greater than 10 or lesser than 20")
# elif a <10:
#         if a<5:
#      print("super lesser")
# else:
#         print("less than 10 bur grearter than 5")
#         print ("after loop completion")
#we cannot have 2 times else statement
#we cannot have elif statement after else 
##==================================================================================================
'''loop statement'''
# a = 10
# icounter = 1
# while icounter  <=10:
#     print(a * icounter)
#     icounter = icounter +1      # table of 10
# ##-------------------------------------------------------------------------------------------------
# alist =[10,43,90,67,60,35,45]
# print (alist[0])        #10
# print (alist[1])        #43
# print (alist[2])        #90
# print (alist[3])        #67
# print (alist[4])        #60
# print (alist[5])        #35
# print (alist[6])        
# print (alist[1])


# print ("hello innovant")
# icounter = 5
# while icounter >0:
#     print("hello innovant")
#     icounter = icounter -1

#alist =[10,43,90,67,60,35,45]
# print (alist[0])

#print ('hello')
#=======================================================================================================
'''while loop'''
# print ("hello innovant")
# print ("hello innovant")
# print ("hello innovant")
# print ("hello innovant")

#icounter = 5

# while icounter >0:                            ##display 5 times hello innovant
#         print ("hello innovant")
#         icounter = icounter -1
# icounter -=1

# icounter = 5 
# while icounter < 0:
#     print ("hello innovant")            
#     icounter = icounter - 1 
# icounter -=1                ##no result


# icounter = 0 
# while icounter <5:
#     print ("hello world")
#     icounter = icounter + 1
# icounter -=1


# num = 10
# print (num * 1)
# print (num * 2)
# print (num * 3)
# print (num * 4)
# print (num * 5)
# print (num * 6)
# print (num * 7)
# print (num * 8)
# print (num * 9)
# print (num * 10)        # table of 10

# icounter = 1 
# while icounter <=10:
#     print (num * icounter)
#     icounter = icounter +1      #using while loop print table of 10

#alist = [10,43,90,67,60,35,45]
# print (alist [0])
# print (alist [1])
# print (alist [2])
# print (alist [3])
# print (alist [4])
# print (alist [5])

# icounter = 0 
# while icounter <=6:
#         icounter <= len (alist)-1
#         print (alist [icounter])
#         icounter = icounter +1      ## display the whole list


# icounter = 0 
# while icounter <=6 :
#     if alist [icounter]==60 or[icounter]==90:
#          print (alist [icounter])
#          icounter = icounter +1

#alist = [10,43,90,67,60,35,45]
# icounter = 0 
# while icounter <= 6 :
#     if alist [icounter] !=60 and alist [icounter] !=90:
#         print (alist[icounter])
#         icounter = icounter +1 

#alist = [10,43,90,67,60,35,45]
# iCounter = 0
# while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
#          if aList[iCounter] == 60 or aList[iCounter] == 90:
#             print(aList[iCounter])
#             iCounter = iCounter + 1 
# print ("hi")

# i = 0
# while i <= 6:
#     if alist [i]== 60 or alist[i]==90:
#         print (alist [i])
#         i=i +1

#         print ("hello")
###=====================================================================================================
'''for loop'''
# alist =[10,45,90,67,60,35,45]
# # for item in alist :
# #     print (item)
# ##============================================================================================
# for item in alist:
#     if item % 2 ==0:
#         print (item)

# ##==============================================================================================
# for item in alist:
#     if item % 2 == 0:
#         print ("even number : ",item)
#     else:
#         print ("odd number :",item)
##==============================================================================================
#user input = int (input("enter number to print all number "))")
#for index in range (10,20,3):
#    print (index)

#for index in range (10,20,2) :
 #   print (index)
###================================================================================================

'''loop statement'''
#alist =[10,43,90,67,60,35,45]
#for item in alist:
#      print (item,end = ' ')
 ##===============================================================================================
# alist = [10,43,45,65,76]
# for item in alist:
#     print (item,end = ' - ')        #10 - 43 - 45 - 65 - 76 - 
#     print()                 ##    10 - 
#                                 # 43 - 
#                                 # 45 - 
#                                 # 65 - 
#                                 # 76 -
# ##--------------------------------------------------------------------------------------------------
# alist = [10,25,35,45,35,23,87]
# for item in alist:
#     print(item,end = ' ')           ##10 25 35 45 35 23 87
#     ##--------------------------------------------------------------------------------------
# alist = [10,25,35,45,35,23,87]
# for item in alist :
#     print(item,end = '/n/n')

# #----------------------------------------------------------------------------------------------
# alist = [13,54,66,88,96,34,65]
# for item in alist:
#     if item ==88:
#         break
#     print(item)         ##break after 88

# ##==-----------------------------------------------------------------------------------------------
# alist = [13,54,66,88,96,34,65]
# for item in alist:
#     if item ==88:
#         continue
#     print(item)         ##skip 88

# #------------------------------------------------------------------------------------------------
# alist = [13,54,66,88,96,34,65]
# for item in alist:
#     print(item)         ##whole list




##================================================================================================
'''range function'''

##====================================================================================================

'''functions'''
##print ()
# input()
#range9
#len()
#print ("hello innovant")
#--------------------------------------------------------------------------------------------------
## we can define functions once and can use multiple time 
##def printInupper():
#     print ("hello innovant".upper())     # hello innovant
# ##-----------------------------------------------------------------------------------------------------
# printInupper()          ##function call    ##trigger
# printInupper()          ##function call    ##trigger
# printInupper()          ##function call    ##trigger
# printInupper()          ##function call    ##trigger
# printInupper()          ##function call    ##trigger
##---------------------------------------------------------------------------------------------
## FUNCTIONS WITH PARAMETER
# we can define functions once and can use multiple lines
#def printInupper(inputstr):
 #   print(inputstr.upper())     #HELLO INNOVANT
#==----------------------------------------------------------------------------------------------
# def printInupper():
#     printInUpper()
# #--------------------------------------------------------------------------------------------------
# def printInupper():
#     print("hello world".upper())
    
##==================================================================================================
'''factorial of  number'''
# counter =5
# result = 1
# while counter >1:
#     result = result * counter
#     counter = counter - 1
#     print ("factorial of 5 :",result)           ##120

##--------------------------------------------------------------------------------------------------

# counter = 2 
# result = 1 
# while counter <=5:
#     result = result * counter
#     counter = counter + 1
#     print("factorial of 5 :",result)            #factorial of 5 : 120

# #------------------------------------------------------------------------------------------------

# factorialofnumber = int(input("enter a number to get factorial :"))
# counter = 2
# result = 1
# while counter <= factorialofnumber:
#     result = result * counter
#     counter = counter +1
#     print("factorial of 5 {factorialofnumber}:{result}")        ##factorial of 5 : 120
          
##================================================================================================

'''syntax error'''

##==================================================================================================
'''exceptions'''
# print("hello")

# print ("hello world")
# a = [10,4,5,20,89]

# print (a [3])
# print (a[5])        #IndexError: list index out of range

#runtime exception : error or exception is occured even though syntax is correct

##program will terminate in case of syntax error  or runtime error.
##-------------------------------------------------------------------------------------------------



##=================================================================================================
'''try and except statement'''

##=============================================================================================

'''custom functions'''                              ##pending
# def isAdultInstring(age : int):
#     if (age >18):
#         return "Adult"
#     else:
#         return "Minor"

# def isAdult (age : int):
#     if (age >18):
#         return True
#     else:
#         return False






##==================================================================================================

'''use function of outside file .py'''

##===========================================================================================
'''reverse list'''
'''assignment'''
# #1. reverse list by using reverse()
# list = [10,4,8,4,9,2,1]
# list.reverse()
# print (list)

# list = [10,4,8,4,9,2,1]
# temp= []
# temp.append(list[len(list)-1])
# print (list)

# for i in range (-1,-len(list)-1,-1):
#     print (list [i])
#     temp.append(list[i])
#     print (temp)

########===========================================================================================

#3. swap first and last element of list.
# list = [10,4,8,4,9,2,1]
# size = len(list)

# temp = list [0]
# list [0]=list [size -1]
# list [size-1]=temp
# print ("list after swapping :",list)

# list = [1,4,8,4,9,2,10]
# temp = list [1]
# list [1]=list [size -2]
# list[size -2]=temp
# print ("list after swapping :",list)

# list = [1,2,8,4,9,4,10]
# temp = list [2]
# list [2]=list [size -3]
# list[size -3]=temp
# print ("list after swapping :",list)

#==========================================================================================
# alist = [10,4,8,4,9,2,1]
# # by using while loop
# def reverse(a):
#     lower =0
#     upper = len(a)-1
#     while lower<upper:
#         temp = alist[lower]
#         alist[lower]=alist[upper]
#         alist[lower],alist[upper]=alist[upper],alist[lower]
#         lower +=1
#         upper -=1
#         return alist
# print (reverse(a))

##=============================================================================================
##reverse String
# string  ="innovant"
# string =string[::-1]
# print(string)           ##tnavonni
# ##=================================================================================================
# string = "i7n3no8va9nt4"
# addition=0
# for item in string :
#     if item.isdigit():
#         print (item)        ##7,3,8,9,4
#     #addition +=int(item)
#     print ("addition : ",addition)
# ##======================================================================================================
#assignment:=
#string = "7n3no8va9nt4"
#print (string[0]+string[2]+string[4]+string[5]+string[7]+ string[8]+string[10]+string[11])
    # innovant

##=================================================================================================  
'''file reading operation'''
# go to the file path or folder and locate file with file name
# open file 
# read containt /write content to the File content
# copy content you got fromm file and use it file close
# try :
#     filevariable = open(r"C:\Users\Sandipan Shinde>my notes.py")
#     filevariable =open("my notes.py")
#     content = filevariable.read()
#     print("file content : ",content)
# except:
#     print("something went wrong")
# finally:
#     filevariable.close()


# try :
#     filevariable = open(r"C:\Users\Sandipan Shinde>sample.txt")
#     filevariable =open("sample.txt")
#     content = filevariable.read()
#     print("file content : ",content)
# except:
#     print("something went wrong")
# #finally:
#  #   filevariable.close()

##=================================================================================================
'''clasess and object'''
# empid =1001
# name = 'komal'
# address = 'pune'
# salary = '3000000'

# def getEmployeeDetails():
#     print (f"Emp id ={empid},name :{name},address:{address},salary:{salary}")
# getEmployeeDetails()

##--------------------------------------------------------------------------------------------------
'''class creation'''
#
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

## self : is a first parameter to method if you want to access class attribute
## self : it is not mandatory to have name as self, it can be anything like selfie or anything
## parameter : when you define function then parameter
## argument  : when you call function then you are providing values, that time argument

# ##----------------------------------------------------------------------------------------------------
# '''object creations'''
# emp = Employee()
# Employee.getEmployeeDetails(emp)
# #mployee.getCompany()
# Employee.getSalary()

# #----------------------------------------------------------------------------------------------------
# emp = Employee()
# emp.getEmployeeDetails(emp)
# emp.getEmployeeDetails()


##=======================================================================================================

'''class with multiple objects.py'''

#class Employee:         # class => keyword to define class , Employee => class name, it can be anything and first char of each word has to be capital
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

##==============================================================================================
'''__init__constructor'''
#----------------------------------------------------------
# class BillingCustomer:
#     billId = 000        # class attribute
#     address = 'Pune'    # class attribute
#     billAmount = 0      # class attribute

#     def getBillingDetails(self):        # method
#         return f"Bill ID : {self.billId}, Address :  {self.address}, Bill Amount : {self.billAmount}"

# billObj = BillingCustomer()         ## Object creation
# billInfo = billObj.getBillingDetails()      # method call by using object
# print(billInfo)     #Bill ID : 0, Address :  Pune, Bill Amount :0

##---------------------------------------------------------------------------------------------------
# class BillingCustomer:
#         billId = 000
#         address = 'pune'
#         billAmount =0

#         def getBillingDetails(self):
#             return f"bill ID : {self.billId},Address : {self.address},Bill Amount :{self.billAmount}"
# billobj = BillingCustomer()
# billInfo = billobj.getBillingDetails()
# print(billInfo)

#----------------------------------------------------------
# class BillingCustomer:
#     billId = 000        # class attribute
#     address = 'Pune'    # class attribute
#     billAmount = 0      # class attribute

#     def getBillingDetails(self):        # method
#         return f"Bill ID : {self.billId}, Address :  {self.address}, Bill Amount : {self.billAmount}"

# billObj = BillingCustomer()         ## Object creation
# billInfo = billObj.getBillingDetails()      # method call by using object
# print(billInfo)     #Bill ID : 0, Address :  Pune, Bill Amount :0

##--------------------------------------------------------------------------------------------------
# class BillingCustomer:
#     billId = 000        # class attribute
#     address = 'Pune'    # class attribute
#     billAmount = 0      # class attribute

#     def __init__(self) -> None:     #self : a class object which is being created
#             self.billId = 111                       # Object attribute
#             self.billAmount = 100                   # Object attribute
#             self.isCorrectionRequired = False       # Object attribute
#             print("I am constructor of BillingCustomer")

#     #Automatically get execute when new object getting created and same object will be passed as arguement to self
#     # init(self,someotherAttribute) having morethan one parameter along with self is a parameterized constructor
#     def __init__(self, id, amount,correction) -> None:     #self : a class object which is being created
#         self.billId = id                       # Object attribute
#         self.billAmount = amount                   # Object attribute
#         self.isCorrectionRequired = correction       # Object attribute
#         print("I am constructor of BillingCustomer")
    
#     def correctionRequired(self):
#         return self.isCorrectionRequired

#     def getBillingDetails(self):        # method
#         return f"Bill ID : {self.billId}, Address :  {self.address}, Bill Amount : {self.billAmount}"

# ###billObj = BillingCustomer()    #__init__()     ## Object creation
# ##TypeError: BillingCustomer.__init__() missing 3 required positional arguments: 'id', 'amount', and 'correction' ##

# billObj = BillingCustomer(111, 200, True)    #__init__()     ## Object creation
# info = billObj.getBillingDetails()  
# print(info) #Bill ID : 111, Address :  Pune, Bill Amount : 200

# billObj2 = BillingCustomer(222, 1000, True)    #__init__()     ## Object creation
# info = billObj2.getBillingDetails()  
# print(info) #Bill ID : 111, Address :  Pune, Bill Amount : 200

# ##-----------------------------------------------------------------------------------------
# # one class can have only one constructor, which will be called everytime when object is beign created.
# # if someone write multiple constructors in same class then last one will be considered and previou one will be overwritten



# def add(a, b, c=0):
#     pass

# add(10,39)     ## no change
# add(10,39)     ## no change
# add(10,39)     ## no change
# add(10,39)     ## no change
# add(10,39)     ## no change
# add(10,39)     ## no change

# add(10, 45, 67)


# # # billObj = BillingCustomer(111, 200, True)      
# # # billObj = BillingCustomer()   '



# ### parameterized contructors

# class Addition:
#     firstNum = 0
#     secondNum = 0

#     def __init__(self, first, second) -> None:  
#         self.firstNum = first
#         self.secondNum = second

#     def getResult(self) -> int:
#         return self.firstNum  + self.secondNum

# ##TypeError: Addition.__init__() missing 2 required positional arguments: 'first' and 'second'
# ##objAdd = Addition()

# objAdd = Addition(20)

##---============================================================================================

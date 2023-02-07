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
alist = [10,20,30,40,50,60,70,80]
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


aList = [10, 43, 90, 67, 60,35,45]
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



iCounter = 0
while iCounter <= 6:        #iCounter < 7  #iCounter <= len(aList) - 1  # iCounter < len(aList)
    if aList[iCounter] != 60 or aList[iCounter] != 90:
        print(aList[iCounter])
    iCounter = iCounter + 1 

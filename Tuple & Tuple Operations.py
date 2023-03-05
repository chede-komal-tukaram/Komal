
# In the tuple (,)is mandatory and round bracket is optional.

# avalue = (10,30,50,55,45,100,95)
# print(avalue,type(avalue))      #class tuple

# avalue=(10)
# print(avalue,type(avalue))      #int

# avalue = (10,30,50,55,45,100,95)
# print(avalue[1])        #30
# print(avalue[-1])        #95

# #tuple is Immutable
# # avalue[4] =0
# avalue =[10,30,50,55,45,100,95]

# avalue.insert(10,2000) 
# print(avalue)               #[10, 30, 50, 55, 45, 100, 95, 2000]
# # it displays only unique records

#*************************************************************************************************************
                                    #Tuple Operations#

#Basically two operation we perform
#1.count 
#2.index


values = (10,20,30,50,60,20,50,60,10,10,100)
# print(values,type(values))

# print(f"avalue before count {values}")
# result = values.count(10)
# print(f"avalue after count {values} : result = {result}")       #(10, 20, 30, 50, 60, 20, 50, 60, 10, 10) : result = 3
#_________________________________________------------------------------------------------
# print(f"values before count():{values}")
# result = values.count(100)
# print(f"values after count(){values} : result = {result}")   #result =1

#-------------------------------------------------------------------------------------------------
# tuple = (10,25,40,60,50,10,100)
# print(f"tuple before index(100)")
# result = tuple.index(100)
# print(f"tuple after index(100){tuple} : result = {result}")   #result =6

# #-------------------------------------------------------------------------------------------
# tuple = (10,25,40,60,50,10,100)
# print(f"tuple before index(25))")
# result = tuple.index(25)
# print(f"tuple after index(25){tuple} : result = {result}")   #result =1

#***********************************************************************************************
#some question about tuple:-
#Q1 write a python code for tuple creation using while/for loop?

# t =()
# n = int(input("Enter any number:"))#5
# i = 1
# while i<=n:
#     print(i)
#     i = i +1

# second method:
# t = ()
# n = int(input("Enter any number:"))#5
# i = 1
# while i<=n:
#     a = int(input("Enter element :"))
#     t = t +(a,)
#     i = i +1
# print("output is:")
# print(t)                #output is:(40, 30, 20, 90, 100)

# third method: usinf for loop
# t = ()
# n = int(input("Enter any number:"))#5

# for i in range (n):
#     a = int(input("Enter element :"))
#     t = t +(a,)
    
# print("output is:")
# print(t)            #(34, 23, 13, 56, 67, 87)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

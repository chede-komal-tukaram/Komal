# num = 10
# icounter = 1
# while icounter <= 10:
#     print(num * icounter)
#     icounter = icounter +1

# list = [10,20,45,65,87,64,89]

# icounter = 0 
# while icounter <=6:
#     icounter <=len(list)- 1
#     print(list[icounter])
#     icounter = icounter +1


# list = [10,20,45,65,87,64,89]

# icounter =0                           #Doughting
# while icounter <= 6:
#     icounter <=len(list)-1
#     print (list[icounter])          
#     icounter = icounter +1

# list = [10,43,90,67,60,35,45]
# icounter = 0
# while icounter <= 6:
#         icounter <= len(list)-1
#         if list [icounter]!= 60 and list [icounter]!=90:
#             print(list[icounter])

#         icounter = icounter +1
# #===========================================================================
list = [10,43,90,67,60,35,45]
icounter = 0
while icounter <= 6:
        icounter <= len(list)-1
        if list [icounter]== 60 or list [icounter]==90:
            print(list[icounter])

        icounter = icounter +1



##******************************************************************************************************
# For Loop:-

# alist = [10,22,33,44,55,66,77]
# for item in alist:
#     print(item)

# for item in alist:
#     if item % 2 == 0:
#         print(item)

# for item in alist:
#     if item % 2 ==0:
#         print("Even Number : ",item)
#     else:
#         print("odd number :",item)

# alist = [10,22,33,44,55,66,77]
# for index in range(44,55,2):
#     print(index)







# some program by using loop:
#Q1. program to sum number from  1 to 10?
# s = 0
# for i in range(1,11):
#     s = s + i
#     print ("sum is  = ", s)     # sum is 55

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Q2. PROGRAM TO PRINT TABLE?
# a = (int)(input("enter a  number"))
# for i in range (1,11):
#     print(a," * ",i," = 1",a * i)       # table of 5

##=========================================================================================
#Q3. PROGRAM TO CALCULATE FACTORIAL?
# a = (int)(input("enter a number :"))
# f = 1
# for i in range (1,a +1):
#     f = f +i
#     print("Factorial is:",f)
#=========================================================================================
#Q4.
# range(5)
# #start point =0
# #condition <5
# # increment 1
# #1,2,3,4

# # range(1,6)
# #start point =0
# #condition <6
# # increment 1
# #1,2,3,4,5

# #range(1,6,2)
# #start point =0
# #condition <6
# # increment 1
# #1,3,5



#1 parameter
# for i in range(5):
#     print("welcome")


# for n in range(1,6):
#     print(n)


# for n in range(1,6,2):
#     print(n)



# for i in range (1,11):
#     print("2*",i,"=",2 * i)
    

# range(10,0,-1)
# for n in range(10,4,-2):
#     print(n)
# =======================================================================
# num = int(input("enter the number:"))
# factorial = 1

# if num<0:
#     print("sorry,factorial for negative number does not exist")
# elif num ==0:
#     print("the factorial for number 0 is ")
# else:
# for i in range(1,num + 1):
#         factorial = factorial * i
#         print("the factorial of ",num,"is",factorial)



# =====================================================

icounter = 0
while icounter <=10:
      if icounter % 2 == 0:
      print(" E")
      icounter = icounter + 1 
-
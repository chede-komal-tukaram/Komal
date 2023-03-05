list =[]

# List is collection of items that are orderd and mutable.
# List can store multiple item and you can change the order and values of the item in the list

#[]- squre bracket
#() - round bracket
#{} - curly bracket


# a = 10
# print(a,type(a))

# colors = ['Red','Green','Blue','Black','Pink']
# print(colors,type(colors))

# avalue = 'welcome'
# avalue[0]

# print(colors[0])        #Red
# print(colors[4])        #Pink
# print(colors[-1])       #Pink
# print(colors[3])        #Black

# print (colors[0:3])     #Red,Green,Blue"""


##=========================================================================================

# colors = ['Red','Green','Blue','Black','Pink']
# newitem = 'white'
# colors[3] = newitem     #item assignement
# colors[4] = 'Yellow'
# print(colors,type(colors))

#avalue ='welcome'
#avalue[3] = 'd'         #TypeError: 'str' object does not support item assignment

#Mutable :- Means changable/we can modify
#Immutable :- non changable / we can't modify

#string - Immutable      # Item assignment is not allowed.
#List - Mutable          #Item assignment is allowed.

#we can not change single or few element/item from list.
#however we can replace whole string

#List - we can change single or few element/item from list.

# avalue = 'welcome'
# print(avalue)
# avalue = 'weldone'
# print(avalue)'''

##============================================================================================


# avalue = 'welcome'
# print(avalue)                   #welcome
# result = avalue.replace('c','d')
# print(avalue)                   #welcome
# print(result)                   #weldome

# avalue = 'welcome'
# print(avalue[::1])              #welcome
# print(avalue[::-1])             #emoclew
# print(avalue[::2])              #wloe
# print(avalue[::-2])             #eolw


# colors =['Red','Green','Blue','Black','Pink']

# print(colors[:])              #['Red', 'Green', 'Blue', 'Black', 'Pink']
# print(colors[::-1])             #['Pink', 'Black', 'Blue', 'Green', 'Red']
# print(colors[::2])              #['Red', 'Blue', 'Pink']
# print(colors[::-2])             #['Pink', 'Blue', 'Red']'''

###*********************************************************************************************************

#List Opeeration#
#1. sort()
#2.reverse()
#3. append()
#4.insert()
#5.pop()
#6.remove()

# colors = ['Red','Green','Blue','Black','Pink']

# values = [34,45,56,89,99,10]

#print(len(colors))      #5

# #1. sort():-
# print(f"List before sort {values}")
# result = values.sort()
# print(f"List after sort {values} : result :{result}")   
# if we want to sort list in ascending manner.


# print(f"List before sort {values}")
# result = values.sort(reverse = True)
# print(f"List after sort {values} : result :{result}")
# if we want to sort list in descending manner.

# #-----------------------------------------------------------------------------------------------------
# #2.reverse():-
# print (f"List before reverse :{values}")
# result = values.reverse()
# print(f"List after reverse {values} : result:{result}")


# #-----------------------------------------------------------------------------------------------

# #print(values[7]) = 100          ##if index is not present you can not do assignment
# #3. append:-

# print(f"List after reverse {values}")       #[10, 34, 45, 56, 89, 99]
# result = values. append(100)
# print(f"List afetr reverse {values}:result :{result}")  #[10, 34, 45, 56, 89, 99, 100]
# # it can be added at the last of the list.
# #----------------------------------------------------------------------------------------------------

# #4.Insert():-
# print(f"List before reverse {values}")      # [10, 34, 45, 56, 89, 99, 100]
# result = values.insert(2,300)
# print(f"List before reverse {values}:result :{result}")     #[10, 34, 300, 45, 56, 89, 99, 100]
# # #insert the value which index we will give to it.

# #--------------------------------------------------------------------------------------
# #5.pop:-
# print(f"List before reverse {values}")      # [10, 34, 45, 56, 89, 99, 100]
# result = values.pop(3)
# print(f"List before reverse {values}:result :{result}")     #[10, 34, 300, 56, 89, 99, 100]:result :45
# #3 is index,value which will be delete from this index and deleted value will be in result variable.

# print(f"List before reverse {values}")      # [10, 34, 45, 56, 89, 99, 100]
# result = values.pop()
# print(f"List before reverse {values}:result :{result}")     #[10, 34, 300, 56, 89, 99]:result :100
# # By default it will poped last index
#--------------------------------------------------------------------------------------------
#6. remove:-
# print(f"List before reverse {values}")      # [10, 34, 45, 56, 89, 99, 100]
# result = values.remove(99)
# print(f"List before reverse {values}:result :{result}")   #[10, 34, 300, 56, 89]:result :None

# print(f"List before reverse {values}")      # [10, 34, 45, 56, 89, 99, 100]
# result = values.remove(300)
# print(f"List before reverse {values}:result :{result}")     #ValueError: list.remove(x): x not in list
#beacause this value is not present on the list


##***************************************************************************************************
# some questions related to list & it's operations
#Q1. How to reverse a list?
# list = [10,20,30,40,50,60,100]
# print(list[::-1])       #[100, 60, 50, 40, 30, 20, 10]

# list1 = ['KOMAL','POOJA','SNEHAL','ASHA','PRIYA']
# print(list1[::-1])      #['PRIYA', 'ASHA', 'SNEHAL', 'POOJA', 'KOMAL']

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# #Q2. How to count an occurence of element in a list?
# list = ['pink','sky blue','white','yellow']
# print(list[3])      #yellow

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11111111

#Q3. find the sum of the list?
# alist = [33,44,54,76,88,15,90]
# total = 0

# for i in range (0,len(alist)):
#     total = total +alist[i]

# print("sum of all elements in given alist",total)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Q4. find odd and even number in a list?
# list = [2,3,4,5,6,7,8,9]
# even = 0
# odd = 0
# for i in list:
#     if (i% 2==0):
#         even = even +1
#     else:
#         odd = odd +1
# print("even number in list ",even)
# print("odd number in list",odd)


##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Q5.write a python program to print duplicate present in the list?
# list = ['hello',10,30,80,45,30,80]
# d=[]
# for element in list :
#     if list.count(element)>1 and element not in d:
#         d.append(element)
# print(d)        #[30, 80]

# # method -2
# list = ['hello',10,30,80,45,30,80]
# d = []
# for i in range(len(list)):
#     for j in range(i + 1,len(list)):
#         if list[i]==list[j] and list[i] not in d:
#             d.append(list[i])
# print(d)            ##[30,80]

##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1#
#Q6.min & max number in the list?
# list = [45,65,55,88,85,95,23,100,10]
# min = list[0]
# max = list [0]

# for i in range (len(list)):
#     if list [i] < min:
#         min = list[i]

#     if list[i] > max:
#         max = list[i]

# print(min)
# print(max)

##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!0
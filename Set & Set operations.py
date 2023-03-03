# list = [10,20,30,10,20]         #duplicate value allowed
# tuple =(10,20,30,40)            #duplicate value allowed
# dictionary ={'key':'value',101:'value'} #duplicate value allowed
# set = {10,20,40,50}             #duplicate value not allowed

#---------------------------------------------------------------------------------------------------

# set = {10,20,60,80,90,20,100}
# print(set,type(set))

# print(len(set)) #6

# set = {10,'a',20,80,'y',(100,True,80),20,None,10}
# print(set)          #{80, 20, 'a', 'y', (100, True, 80), 10, None}

# set = {10,'a',20,80,'y',(100,True,80),20,None,10}
# print(set)

#========================================================================================================
#Set Operations#
#1. Remove()
# set = {10,30,40,50,30,40,20}
# print(f"set before remove :{set}")
# result = set.remove(10)
# print(f"set after remove :{set} :result :{result}") # 10 removed and duplicate also remove

#----------------------------------------------------------------------------------------

#2.pop()

# set = {10,30,40,50,30,40,20}
# print(f"set before pop :{set}")
# result = set.pop()
# print(f"set after pop :{set} :result :{result}")        #{20, 40, 10, 30} :result :50

#-------------------------------------------------------------------
#3.clear()

# set = {10,30,40,50,30,40,20}
# print(f"set before clear :{set}")
# result = set.clear()
# print(f"set after clear :{set} :result :{result}")       #11 None

#---------------------------------------------------------------------------------
#4.Union

# set = {10,30,40,50,30,40,20}
# print(f"set before pop :{set}")
# result = set.union({50,200,55})
# print(f"set after pop :{set} :result :{result}")       #{50, 20, 40, 10, 30} :result :{50, 20, 55, 40, 10, 30, 200}

#--------------------------------------------------------------------------------\
#Intersect
# set = {10,20,40,80,100,50}

# print(f"set before pop :{set}")
# result = set.intersection({50,200,55})
# print(f"set after pop :{set} :result :{result}")       # result = 50

##=============================================================================================================

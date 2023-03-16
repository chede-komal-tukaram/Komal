#10 + 10 =20
# print(10 + 10)          #20
# print("10" + "20")      #1020

# print(10 + "20")    #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# #--------------------------------------------------------------------------
# avalue = 10 
# bvalue = 20
# print(avalue + bvalue)      #30

# #----------------------------------------------------------------------------------------------------
# avalue = "10"
# bvalue = "20"
# print(avalue + bvalue)      #1020
# #----------------------------------------------------------------------------------------------------

# int() => take input and create copy and convert in int then provide output

# avalue = 10
# bvalue = "20"
# print(avalue + int(bvalue))     #30
# # ===================================================================================
# # str():- take input and create copy and convert str then provide output
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

# avalue = "Innovant"
# print(type(eval(avalue)))       #error
# print (eval(avalue))

# avalue = ""
# print(type(eval(avalue)))       #error
# print (eval(avalue))            # syntaxerror


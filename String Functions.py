#some points of stiring functions:-
#1. a string can used by starts with or endswith .
#2.in string function letter is case sensetive always write letter as it is like a strig present.
# capitalize()
#upper()
#lower()
#find()
#replace()

# avalue = "sandip shinde"

# print(f"Length of avalue : {len(avalue)}")

# result = avalue.startswith('S')
# print(f"{avalue}Startswith 'S' : {result}")     #False

# result = avalue.startswith('s')
# print(f"{avalue}Startswith 's' : {result}")     #TRUE

# result = avalue.startswith('s')
# print(f"{avalue}Startswith 's' :{result}")
#--------------------------------------------------------------------------------------------------

# result = avalue.endswith('shinde')
# print(f"{avalue} endswith 'shinde':{result}")       #True
# __________________________---------------------------------------------------------------------

# value = "welcome"
# result = value.capitalize()
# print(f"{value} capitalize():{result}")     #welcome capitalize():Welcome


# result = value.upper()
# print(f"{value} upper():{result}")          #welcome upper():WELCOME

# result = value.lower()
# print(f"{value} lower():{result}")          ##welcome lower():welcome
#--------------------------------------------------------------------------------------------

# avalue = 'hello world'

# result = avalue.find('world')
# print(f"Index of 'world' in {avalue} :{result}")    #6

# result = avalue.find('world',2)
# print(f"Index of 'world' in {avalue} :{result}") 

# result = avalue.find('world',2,5)
# print(f"Index of 'world' in {avalue} :{result}") 

# result = avalue.find('r',2)
# print(f"Index of 'r' in {avalue} :{result}") #8

#-------------------------------------------------------------------------------------------------------
# value = "hello world"
# result = value.replace('world','komal')
# print(f"replace 'come' with 'komal' in {value} : {result}")     #hello komal

# result = value.replace('world','komal').replace('komal','kalyani').upper()
# print(f"replace('world' with 'kalyani' in {value} : {result}")      #HELLO KALYANI

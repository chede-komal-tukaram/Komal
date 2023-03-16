
#we can write many more attribute in only one function.
# def somefunctions(id,name,address,contact,pincode,interest,food,landline):
#     print("nothing....",id,name)

# somefunctions (10,'name','pune',"NA","NA","NA","NA","NA", )


# class employee():
#     id = 10,
#     name = 'komal',
#     address = 'pune',
#     contact = "NA",
#     pincode = "NA",
#     interest ="NA",
#     food = "NA",
#     landline = "NA"

# emp = employee()
# emp.contact = "do not contact me"

# def somefunction(emp):
#         print("nothing....",emp.id,emp.name,emp.contact)
# somefunction(emp)

# ##create a function which accept list or tuple variable.

# def iAcceptAnyNumberofparameter(name):
#         return name

# print(iAcceptAnyNumberofparameter("pooja"))     #POOJA

# iAcceptAnyNumberofparameter("pooja")

# print(print(iAcceptAnyNumberofparameter("pooja")))  #POOJA NONE
    
# def iAcceptAnyNumberofParameter(name):
#       print(name)

# iAcceptAnyNumberofParameter("pooja")    #pooja
# print(iAcceptAnyNumberofParameter("pooja")) #pooja none

#-----------------------------------------------------------------------

# def iAcceptAnyNumberofParameter(name,name2 ='',name3 =''):
#       print(name,name2,name3)


# # iAcceptAnyNumberofParameter()
# iAcceptAnyNumberofParameter("pooja")    #pooja
# iAcceptAnyNumberofParameter("pooja","komal") #pooja komal
# iAcceptAnyNumberofParameter("pooja","komal","priya") #pooja komal,priya
# # iAcceptAnyNumberofParameter("pooja","komal","priya","sakshi") #error

# #-------------------------------------------------------------------------------------

##    *is used for pack and unpack tuple
# def iAcceptAnyNumberofParameters(*name):
#     print(*name)

# iAcceptAnyNumberofParameters("pooja")    #pooja
# iAcceptAnyNumberofParameters("pooja","komal") #pooja komal
# iAcceptAnyNumberofParameters("pooja","komal","priya") #pooja komal,priya
# iAcceptAnyNumberofParameters("pooja","komal","priya","sakshi") #
# iAcceptAnyNumberofParameters("pooja","komal","priya","sakshi","pooja","komal","priya") #


# ====================================================================================================
###Q . write a function which can accept n number of arguments

# def iAcceptAnyNumberofParameters(*name):
#       print(*name)
     
# iAcceptAnyNumberofParameters()

# iAcceptAnyNumberofParameters("pooja")
# iAcceptAnyNumberofParameters("pooja","komal")
# iAcceptAnyNumberofParameters("pooja","komal","priya")
# iAcceptAnyNumberofParameters("pooja","komal","priya","snehal")
# iAcceptAnyNumberofParameters("pooja","komal","priya","snehal","reva")
# iAcceptAnyNumberofParameters("pooja","komal","priya","snehal","reva","kalyani")
# iAcceptAnyNumberofParameters("pooja","komal","priya","snehal","reva","kalpana","shreya")
# iAcceptAnyNumberofParameters("pooja","komal","priya","snehal","reva","sunita","shreya","sandhya")

# Tuple = ("pooja","komal","priya","asha")
# print(Tuple)        #print as tuple
# print(*Tuple)       #unpack the tuple

# #==========================================================================
# # only one  "*" parameter allowed
# ##def packing(*name,*number):
# #only one "*" parameter allowed
# ##print(name,number)


# def packing(*name,number):      #only one "*"allowed
#       print(name,number)

# packing("pooja","priya","kalpana")
# # TypeError: packing() missing 1 required keyword-only argument: 'number'
      
# packing("pooja","priya","kalpana", number =10)
# #typeError: packing() missing 1 required keyword-only argument: 'number'


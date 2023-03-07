# class BillingCustomer:
#     billId = 000            #class attribute
#     address = 'pune'        #class attribute
#     billAmount = 0          #class attribute
    
#     def getBillingDetails(self):            # we call function as method in the class
#         return f" bill id :{self.billId},address :{self.address},billAmount :{self.billAmount}"

# billObj = BillingCustomer()                 # object creation
# billInfo = billObj.getBillingDetails()      # method call by using object
# print(billInfo)                             #bill id :0,address :pune,billAmount :0


# ========================================================================================

# constructors:-

# class BillingCustomer:          #class is keyword, BillingCustomer is class name
#     billid = 111
#     address = 'solapur'
#     billamount =100

#     def __init__(self) ->None:                  #self
#         print("I AM CONSTRUCTOR OF BILLING CUSTOMER")

#     def getBillingDetails(self):
#         return f" bill id :{self.billid},Address :{self.address},billamount :{self.billamount}"
    
# billobj = BillingCustomer()         #object creation
# billobj.billid =222
# billobj.billamount = 200
# billInfo =billobj.getBillingDetails()       #method
# print(billInfo)


# billobj2 =BillingCustomer()
# billobj2.billid = 333
# billobj.billamount = 444
# billInfo = billobj.getBillingDetails()
# print(billInfo)


##=========================================================================================
#constructor:-
# class BillingCustomer:
#     billid = 123
#     address = "karmala"
#     billAmount = 200

# #Automaticallly get executed when new object getting created and same object will be passed as 
# # argument to self
# #init(self) having only onne parameter which is a default constructor.

#     def __init__(self) -> None:         #self : a class object which is being created 
#         self.billid = 333
#         self.billaddress = "pune"
#         self.billamount = 555

#         self.isCorrectionRequired = False           #object attribute
#         print("i am constructor")

#     def getBillingDetails(self):
#             return f" bill id :{self.billid}, billaddress : {self.billaddress},billamount :{self.billamount}"
        
# billobj = BillingCustomer()
# billInfo = billobj.getBillingDetails()          #Method call by using object
# print(billInfo)


# billobj2 = BillingCustomer()
# billInfo = billobj2.getBillingDetails()             #method call by using object
# print(billInfo)


# billobj.__init__()          #mannual way to call constructor

# billobj2.__init__()         #mannual way to call constructor

##=========================================================================================
# class BillingCustomer:
#     billid = 500
#     address = 'solapur'
#     company = "IBM"

#     def __init__(self) -> None:
#         self.billid = 111
#         self.billamount = 500
#         self.company = "IBM"

#         self.isCorrectionRequired = False
#         print("I am komal sandip shide")

#     def __init__(self,id,amount,company,correction)->None:
#         self.billid = id
#         self.amount = amount
#         self.company = company
#         self.isCorrectionRequired = correction
#         print("I am komal tukaram chede")

#     def correctionRequired(self):
#         return self.isCorrectionRequired
#     def getBillingDetails(self):
#         return f"Billid : {self.billid},address: {self.address},company:{self.company}"
    
# # ##billobj = BillingCustomer()
# ##__init__()      #TypeError: BillingCustomer.__init__() missing 4 required positional arguments: 'id', 'amount', '


# billobj = BillingCustomer(111,200,"IBM",True,)
# # __init__()
# info = billobj.getBillingDetails()          #Billid : 111,address: solapur,company:IBM
# print(info)



# billobj2 = BillingCustomer(111,200,"IBM",True,)
# # __init__()
# info = billobj2.getBillingDetails()         #Billid : 111,address: solapur,company:IBM
# print(info)
# #================================================================================================
# # one class have only one constructor ,which will be called everytime when object is being created.
# #if someone write multiple constructor in same class then last one will be considered and provode one will be overwritten


# def add (a,b, c = 0):
#     pass

# add (10,39)
# add (10,39)
# add (10,39)
# add (10,39)
# add (10,39)
# add (10,39)
# add (10,39)
# add(10,45,67)

# billobj = BillingCustomer(111,200,"IBM",True)
# billobj = BillingCustomer()

# #3==============================================================================================

# ##PARAMETERIZED CONSTRUCTOR

# class Addition:
#     firstnum = 0
#     secondnum = 0
#     def __init__(self,first,second)-> None:
#         self.firstnum = first
#         self.secondnum = second
#     def getResult(self)->int:
#         return self.firstnum + self.secondnum
    
# objAdd = Addition(200,300)
# print(objAdd.getResult())

##=============================================================================================
# parameterized constructor:
# class Addition:
#     firstnum = 0
#     secondnum = 0 
#     def __init__(self,first = 100,second = 100)-> None:
#         self.firstnum = first
#         self.secondnum = second
#     def getResult(self) -> int:
#         return self.firstnum+ self.secondnum
    
# objadd = Addition(200,300)
# print(objadd.getResult())       #500

# objadd = Addition()
# objadd =Addition(400)
# objadd = Addition(second = 500)
# objadd = Addition(second= 500,first = 300)

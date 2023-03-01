# class BillingCustomer:
#     billId =000
#     address = 'pune'
#     billAmount = 0

#     def getBillingDetails(self):
#         return f"Bill Id :{self.billId},Address: {self.address},Bill Amount : {self.billAmount}"
    
# billobj =BillingCustomer()
# billInfo = billobj.getBillingDetails()
# print(billInfo)

# ##========================================

# class BillingCustomer:
#     billId = 000
#     address = 'pune'
#     billAmount = 0
    
#     def __init__(self) ->None:
#         print("I am constructor of BillingCustomer")

#     def getBillingDetails(self):
#         return f"Bill Id :{self.billId},Address:{self.address},billAmount : {self.billAmount}"
    
# billobj =BillingCustomer()
# billobj.billId = 111
# billobj.billAmount = 100
# billInfo = billobj.getBillingDetails()
# print(billInfo)


# billobj2 = BillingCustomer()
# billobj2.billId =222
# billobj2.billAmount =200
# billInfo = billobj2.getBillingDetails()
# print(billInfo)
##----------------------------------------------------------------------------------------

# class BillingCustomer:
#     billId = 000
#     address = "pune"
#     billAmount =0

#     def __init__(self) ->None:
#         self.billId = 111
#         self.billAmount = 100
#         self.isCorrectionRequired = False
# print("I am constructor of BillingCustomer")

# def getBillingDetails(self):
#     return f"Bill Id :{self.billId},Address :{self.address},Bill Amount:{self.billAmount}"

# billobj = BillingCustomer()
# #billInfo =billobj.getBillingDetails()
# print("billInfo")

# billobj2 = BillingCustomer()
# #billInfo=billobj2.getBillingDetails()
# print(billInfo)

# billobj.__init__()
# billobj2.__init__()

# ##--------------------------------------------------------------------------------

# def add(a,b, c=0):
#     add(10,39)
#     add(10,39)
#     add(10,39)
#     add(10,39)
#     add(10,39)
#     add(10,39)

# add (10,45,67)

# billobj = BillingCustomer(111,200,True)
# billobj = BillingCustomer()


##===============================
#parameterized constructor :


# class Addition:
#     firstNum =0
#     secondnum =0

#     def __init__(self,first,second) -> None:

#         self.firstnum = first
#         self.secondnum = second

#     def getResult(self) ->int:
#         return self.firstnum + self.secondnum

# #objAdd = Addition()

# objAdd = Addition(200,300)
# print(objAdd.getResult())


# # -----------------------------------------------------------------------------------------------------------
# #parameterized constructor

# class Addition:
#     firstnum =0
#     secondnum =0
#     def __init__(self,first = 100,second =100) -> None:
#         self.firstnum = first
#         self.secondnum = second

#     def getResult(self) -> int:
#         return self.firstnum +self.secondnum
    
# objAdd = Addition()
# objAdd = Addition (200,300)
# print(objAdd.getResult())

# objAdd =Addition()
# objAdd =Addition(400)
# objAdd =Addition(second =500)
# objAdd =Addition(second = 500,first =300)

###========================================================================================================================
#Exceptions:
print("hello world")

# a = [10,34,54,22,88]
# try:
#     print(a[3])
#     print(a[2])
#     print(a[0])
#     print(a[-1])
#     print(a[6])
# except Exception as ex:
#     print("something went wrong",ex)

# print("program is compleated...")


# ##===========================================================================================
# a = [10,45,34,22,4,5]
# try :
#     print(a [3])
#     print(a[2])
#     print(a[6])
#     print(a[0])
#     print(a[-1])
# except Exception as ex :
#     print("something went wrong",ex)
# print("program is compleated...")

##===================================================================
# a = [10,4,65,4,32]
# try :
#     print(a [3])
#     print(a[2])
#     print(a[6])
#     print(a[0])
#     print(a[-1])
# except Exception as ex :
#     print("something went wrong",ex)
# print("Given index is not present",ie)
# print("program is compleated")
# ##====================

# try:
#     inputnumber = input("enter number to divide to 100 :")
#     result = 100/int(inputnumber)
#     print("result : ",result)

# except ZeroDivisionError as z :
#     print("You can not enter 0 as input :",z)
# except ValueError as v:
#     print("Input value is invalid",v)
# except Exception as ex :
#     print("Error occured :",ex)




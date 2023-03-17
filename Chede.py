# class BillingCustomer:        #BillingCustomer is a class name
#     billId = 000              #attribute
#     address = 'pune'          #attribute
#     billAmount = 0            #attribute

#     def getBillingDetails(self):
#         return f" BILL ID : {self.billId}, ADDRESS : {self.address},BILLAMOUNT :{self.billAmount}"
    
# billobj = BillingCustomer()
# billInfo = billobj.getBillingDetails()
# print(billInfo)             #BILL ID : 0, ADDRESS : pune,BILLAMOUNT :0



# ================================================================
# #constructors:
# class BillingCustomer:
#    billId = 111
#    address = 'pune'
#    billAmount =222

#    def __init__(self) -> None:
#         print("I am constructor of this BillingCustomer")

#    def getBillingDetails(self):
#        return f"billId :{self.billId},address : {self.address}, billAmount :{self.billAmount}"

# billobj = BillingCustomer()
# billobj.billId = 222
# billobj.billAmount = 100
# billInfo = billobj.getBillingDetails()
# print(billInfo)     #billId :222,address : pune, billAmount :100

#=====================================================================================
##constructor:
# class BillingCustomer:
#     billId = 121
#     address = 'solapur'
#     billAmount = 211

#     def __init__(self) -> None:
#             self.billId=333
#             self.billAmount =444
#             self.isCorrectionRequired = False
#             print("I am constructor of BillingCustomer")

#     def getBillingDetails(self):
#          return f"bill Id : {self.billId},address : {self.address},billAmount : {self.billAmount}"

# billobj = BillingCustomer()
# billInfo = billobj.getBillingDetails()
# print(billInfo)
# print(billobj)

# billobj2 = BillingCustomer()
# billInfo = billobj2.getBillingDetails()
# print(billInfo)
# # =============================================================================================
# class BillingCustomer:
#       billId = 000
#       address = 555
#       billAmount =000

# def __init__(self) -> None:
#             self.billId=333
#             self.billAmount =444
#             self.isCorrectionRequired = False
#             print("I am constructor of BillingCustomer")

# def __init__(self,id,amount,correction) ->None:
#        self.billId = id
#        self.billAmount = amount
#        self.isCorrectionRequired = correction
#        print("I am constructor of BillingCustomer")
# def correctionRequired(self):
#        return self.isCorrectionRequired

# def getBillingDetails(self):
#        return f" bill id :{self.billId},Address : {self.address},bill amount :{self.billAmount}"

# # billobj = BillingCustomer()
# # __init__()                TypeError:

       
# # billobj = BillingCustomer(111,200,True)
# # __init__()
# # info = billobj.getBillingDetails()
# # print(info)

# billobj2 = BillingCustomer(222,1000,True)
# INFO = billobj2.getBillingDetails()
# print(INFO)



##=====================================================================================================
# class creation 
# class Employee:
#     empid = 1001
#     name = 'komal'
#     address = 'pune'
#     salary = '500000'

#     def getEmployeeDetails(self):
#         print(f"Empid : {self .empid},name : {self.name},address : {self.address},salary : {self.salary}")

#     def getCompany():
#         print("Innovant")

# emp = Employee()
# emp.getEmployeeDetails()    #Empid : 1001,name : komal,address : pune,salary : 500000

# class TempEmployee(Employee):
#     duration = 12

#     def getduration(self):
#         print(f"duration:{self.duration}")

# tempEmp = TempEmployee()
# tempEmp.getEmployeeDetails()    #Empid : 1001,name : komal,address : pune,salary : 500000
# tempEmp.getduration()           #duration:12
# Employee.getCompany()           #Innovant
# emp.getEmployeeDetails()        #Empid : 1001,name : komal,address : pune,salary : 500000

# # emp.getduration()

# #Multiple inheritance
# class ConsultantEmployee(Employee,TempEmployee):


# ========================================================================
# single inheritance:

# class Employee:
#     name = 'unknown'
#     address = 'unknown'

#     def getEmployeeDetails(self):
#         print(f"name :{self.name},address : {self.address}")

# class TempEmployee(Employee):
#     stipend =100000

#     def getstipend(self):
#         print(f"stipend : {self.stipend}")

# empobj = Employee()
# empobj.getEmployeeDetails()

# tempEmp = TempEmployee()
# tempEmp.getEmployeeDetails()
# tempEmp.getstipend()


##---------------------------------------------------------------------------------------------

# Multilevel inheritance:-

# class Employee:
#     name = 'unknown'
#     address = 'unknown'

#     def getEmployeeDetails(self):
#         print(f"name :{self.name},address : {self.address}")

# class TempEmployee(Employee):
#     stipend =100000

#     def getstipend(self):
#         print(f"stipend : {self.stipend}")

# empobj = Employee()
# empobj.getEmployeeDetails()

# tempEmp = TempEmployee()
# tempEmp.getEmployeeDetails()
# tempEmp.getstipend()

# class InternEmployee(TempEmployee):
#     duration = 6 

#     def getdurationMonth(self):
#         print(f"durationMonth :{self.durationMonth}")

# objIntern =InternEmployee()
# objIntern.getEmployeeDetails()
# objIntern.getstipend()
# # objIntern.getdurationMonth()

##------------------------------------------------------------------------------

## heirarchial inheritance
class Employee:
     
    name = 'unknown'
    address = 'unknown'

    def getEmployeeDetails(self):
        print(f"name :{self.name},address : {self.address}")

class TempEmployee(Employee):
    stipend =100000

    def getstipend(self):
        print(f"stipend : {self.stipend}")

empobj = Employee()
empobj.getEmployeeDetails()

tempEmp = TempEmployee()
tempEmp.getEmployeeDetails()
tempEmp.getstipend()

class InternEmployee(TempEmployee):
    duration = 6 

    def getdurationMonth(self):
        print(f"durationMonth :{self.durationMonth}")

objIntern =InternEmployee()
objIntern.getEmployeeDetails()
objIntern.getstipend()
# objIntern.getdurationMonth()

# =---------------------------------------------------------------------------------------
'practise of class and object '

id = 1001
name = 'komal'
address = 'pune' 
salary ='50000'

def getEmployeeDetails():
    print(f"id ={id},name :{name},address:{address},salary :{salary}")

    getEmployeeDetails()            # it does not disply result
#-----------------------------------------------------------------------------------------------

# class creation
class Employee:
    empid =1001
    name ='Savan'
    address = 'pune'
    salary = '50000'

    def getEmployeeDetails(komal):
        print(f"empid : {komal.empid},name :{komal.name},address :{komal.address},salary:{komal.salary}")
        
    def getcompany():
        print("Innovant")

Employee.getcompany()
# Employee.getEmployeeDetails()
print(Employee.salary)
# ------------------------------------------------------------------------------------------------
#  object reation:-
emp = Employee()
Employee.getcompany()
emp = Employee()
# emp.getEmployeeDetails(emp)
emp.getEmployeeDetails()

# ======================================================================
# class creation
class Employee:
    empid = 1001
    name = 'kalyani'
    address = 'pune'
    salary = '60000'

    def getInfo(self):
        print(f"empid = {self.empid},name:{self.name},address :{self.address},salary :{self.salary}")
     
    def updateInfo(selfie,empid,name,company):
        selfie.empid =empid
        selfie.name = name
        selfie.company = company


emp =Employee()
emp2 = Employee()
emp.getInfo()
emp2.getInfo()

Employee.updateInfo(emp,2002,'priya','IBM')

emp.getInfo()
emp2.getInfo()

print(emp.company)
print(emp2.company)
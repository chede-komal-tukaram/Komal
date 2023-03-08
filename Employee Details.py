class Employee:
    empid = 1001
    name = 'komal'
    address = 'pune'
    salary = '50000'

    def getInfo(self):
        print(f"Emp id :{self.empid},name :{self.name},address :{self.address},salary :{self.salary}")
    
    def updateInfo(self,empid,name,address):
        self.empid = empid
        self.name = name
        self.address = address

emp = Employee()
emp2 =Employee()


emp.getInfo()           #Emp id :1001,name :komal,address :pune,salary :50000
emp.updateInfo(2002,'kalyani','solapur')
emp.getInfo()           #Emp id :2002,name :kalyani,address :solapur,salary :50000

emp2.getInfo()
emp2.address = 'delhi'

print("Class Level Changes")
Employee.empid = 3333
Employee.name = "class level changes"
Employee.salary = '9999999'
Employee.address = "UK"

emp.getInfo()       #Emp id :2002,name :kalyani,address :solapur,salary :9999999
emp2.getInfo()      #Emp id :3333,name :class level changes,address :delhi,salary :9999999 


###============================================================================================

#if you are doing class level changes 
#1. check  attribute present in object,if it modified than default values.
#then do not aplly class level changes.
# if attribute is not modified then apply class level changes.


# emp.company ##ERROR
# emp.comapany = "innovant"
# emp.company #NO ERROR SINCE WE HAVE ADDED COMPANY ATTRIBUTE TO EMP OBJECT
# emp2.company## error



###==========================================================================================
# class creation 
class Employee:             #class:- keyword to definne class, Employee :- class name, it can be anything and first char of each word has to be capital

    empid = 1001            #attribute
    name = 'komal'            #attribute
    address = 'pune'            #attribute
    salary ='500000'            #attribute

    def getEmployeeDetails(self):       #method defination #user defined
        print(f"Empid :{self.empid}, name :{self.name},address : {self.address},salary : {self.salary}")

    def getCompany():       #self need to pass only when we need to use class attribute
        print("Innovant")

emp = Employee()
emp.getEmployeeDetails()


class TempEmployee(Employee):       # TempEmployee child class #Employee parent/Base
    Duration = '12'                 #attribute 12 month


    def getDuration(self):
        print(f"Duration : {self.Duration}")

tempEmp =TempEmployee()
tempEmp.getEmployeeDetails()        # this method is inherited from parent/base class # Employee
tempEmp.getDuration()

emp.getEmployeeDetails()

# you cannot access property of child class into base class
emp.getDuration()


# MULTIPLE INHERITANCE

# class ConsultantEmployee(Employee,TempEmployee):    # Tempemployee child class #employee arent/base class
    # duration = 12  ATTRIBUTE


# =================================================================================================

# Single Inheritance:-
class Employee:
    name = "Unknown"
    address = "Unknown"

    def getEmployeeDetails(self):
        print(f" name : {self.name},address : {self.address}")

class TempEmployee(Employee):
    stipend = 100000

    def getStipend(self):
        print(f"Stipend : {self.stipend}")

empobj = Employee()
empobj.getEmployeeDetails()


tempEmp = TempEmployee()
tempEmp.getEmployeeDetails()
tempEmp.getStipend()
#===========================================================================================

# Multilevel Inheritance:-
class Employee:
        name = "Unknown"
        address = "Unknown"

        def getEmployeeDetails(self):
            print(f" name : {self.name},address : {self.address}")

class TempEmployee(Employee):
    stipend = 100000

    def getStipend(self):
        print(f"Stipend : {self.stipend}")

empobj = Employee()
empobj.getEmployeeDetails()


tempEmp = TempEmployee()
tempEmp.getEmployeeDetails()
tempEmp.getStipend()

class InternEmployee(TempEmployee):
     DurationMonth = 6

     def getDuraionMonth(self):
          print(f"DurationMonth : {self.DurationMonth}")

objIntern = InternEmployee()
objIntern = getEmployeeDetails()
objIntern.getStipend()
objIntern = getDurationMonth()


# =======================================================================================

#heirarchial inheritance:-

class Employee:
    name = "unknown"
    address = "unknown"

    def getEmployeeDetails(self):
        print(f" Name: {self.name},address : {self.address}")

class TempEmployee(Employee):
    stipend= 20000

    def getStipend(self):
        print(f"Stipend : {self.stipend}")

empobj = Employee()
empobj.getEmployeeDetails()

tempEmp = TempEmployee()
tempEmp.getEmployeeDetails()


class InternEmployee(Employee):
    durationMonth = 6
    def getdurationMonth(self):
        print(f"durationMonth :{self.durationMonth}")

objIntern = InternEmployee()
objIntern.getEmployeeDetails()
objIntern.getdurationMonth()
    
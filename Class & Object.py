empid = 1001
name = 'komal'
address = 'pune'
salary = '50000'

def getEmployeeDetails():           #function defination *user defined
    print(f"Emp id ={empid},Name :{name},address :{address},salary :{salary}")  #function body

getEmployeeDetails()                  #function call

#-------------------------------------------------------------------------------------------------
##class creation
class Employee:         #class keyword is defined to class,
                            #Employee is class name,it can be anything and first char of each word has to be capital

        empid =2002             #attribute
        name = 'sandip'         #attribute
        address = 'pune'        #attribute
        salary = '60000'       #attribute
        
        def getEmployeeDetails(self):           #method defination
              print(f"Emp id = {self.empid},name :{self.name},address :{self.address},salary :{self.salary}")
      
        def getCompany():           #self need to pass only when we need to use class attribute
              print("Innovant")

Employee.getCompany()        #way to call class method
##Employee.getEmployeeDetails()       #TypeError: Employee.getEmployeeDetails() missing 1 required positional argument: 'self'
print(Employee.salary)


# self is first parameter to method if you want to access class attribute
#self:it is not mandatory to have name as self,it can be anything like selfie or anything.
#parameter : when you define function then parameter.
#argument : when you call function then you are  providing values, that time argument.
#----------------------------------------------------------------------------------------------

# object creation#

#first approtch to call method by using class name.
# emp = Employee()            #Employee is class and emp is object emp is just object name it can be anything
# Employee.getEmployeeDetails(emp)            #we are passing emp object of employee type to method as self argument
# Employee.getCompany()

#---------------------------------------------------------------------------------------------------
#second approtch to call method by using class object.
emp = Employee()    #Employee is class and emp is object..emp os just object name,it can be anything
emp.getEmployeeDetails()      #takes 1 positional argument but 2 were given 
emp.getEmployeeDetails()


##***************************************************************************************************
#CLASS WITH MULTIPLE OBJECTS#


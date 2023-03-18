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

# # =---------------------------------------------------------------------------------------

# # 
# from selenium.webdriver.common.by import By
# from pageObject.ConfirmPage import confirmpage

# class CheckOutPage:

#     def __init__(self, driver):
#         self.driver = driver

#     # driver.find_elements_by_css_selector(".card-title a")
#     # driver.find_element_by_xpath("//button[@class='btn btn-success']")
#     cardTitle = (By.CSS_SELECTOR, ".card-title a")
#     cardFooter = (By.CSS_SELECTOR, ".card-footer button")
#     checkOut = (By.XPATH, "//button[@class='btn btn-success']")

#     def getCardTitles(self):
#         return self.driver.find_elements(*CheckOutPage.cardTitle)

#     def getCardFooter(self):
#         return self.driver.find_elements(*CheckOutPage.cardFooter)

#     def checkOutItems(self):
#         self.driver.find_element(*CheckOutPage.checkOut).click()
#         confirmPage = ConfirmPage(self.driver)
#         return confirmPage


#####88888888888888888888888888888888888888888888888888888888888888888888888888888888888888

import pytest
from selenium import webdriver
import time
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

## this fixture will execute every time when we are using BaseClass
@pytest.fixture(scope="class") ## scope ="class" means this fixture can be used on class not on method          ## Fixture scope can be class or method
def setup(request):
    global driver
    ## below line is working as input
    browser_name=request.config.getoption("browser_name")   #pytest --browser_name "firefox"
     # parameter which can be passed with pytest command
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    elif browser_name == "safari":
        print("Safari driver")
    else:
        driver = webdriver.Chrome()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    ## cls => class => fixture attached class or a class which is using this fixture For now BaseClass
    ## adding attribute driver to BaseClass and assing value of driver we created here
    request.cls.driver = driver         ## request => to class which is using fixture
    yield
    driver.close()
##scope – The scope for which this fixture is shared; one of ``"function"`` (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.

# This hook is used to take automatically screenshot and place in HTML report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    global driver
    driver.get_screenshot_as_file(name)


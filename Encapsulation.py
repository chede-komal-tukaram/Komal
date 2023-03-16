class dad():        #Inheritance..Dad class inherited from Human(abstract class)..so we need to define
                    #or implement all abstract method present in human class.
    sampatti ='Jaminjaydad'
    publicpassword ='1234'              #public attribute
    __accountpass = 'privatepassword'   #privateattribute when we provide__ double underscore before 
                                        #attribute name
    _childpass = 'protectedpassword'    #protected attribute when we provide _ single underscore before
                                        #attribute name
    def __init__(self) -> None:         #as soon as object gets created and before assign to object 
                                        #variable in left side
        print("dad init")

        def bankAccount(self,password):
            if self.__accountpass == password:
                print("account is malamal")
            elif self._childpass == password:
                print("money withdraw limit is 1k per day")
            else:
                print("padhai karo..pahila numbaer lao then try to access")
        def getpassword(self):              #getter  #read only private attribute  # public method inside 
                                            #we are  accessing private attribute 
            return self.__accountpass
        
        def setpassword(self, oldpass,newpass): #setter  #to update private attribute in restricted way/
                                                #in controlled manner

            if oldpass == self.__accountpass:
                self.__accountpass = newpass
            else:
                print("please enter correct password")


class mom():
    def __init__(self) ->None:
        super().__init__()          #human init super points to base class which human
        print("mom cooking")        #mom cooking

    def speak(self):
        print("speak hindi")

    def walk(self):
        print("slow walk")


class Beta(dad):
    def __init__(self) -> None:
        super().__init__()
        print("beta init")

beta = Beta()
print(beta.sampatti)        #jaminjaydad inherited from base class dad
#beta.bankAccount('1234')      #Error

print(beta.publicpassword)
# beta.bankAccount(beta.publicpassword)   #'erro'

# we can not access private attribute  of any class outside of that class

#print(beta.__accountpass)   #'beta' object has no attribute __accountpass'.
# print(dad.__accountpass)    #dad has no attribute __accountpass

#dad = dad()

#print(dad.__accountpass)   #dad has no attribute __accountpass

# '__accountpass'.beta.bankAcount('1234')

print(beta. _childpass)
print(dad._childpass)
dad = dad()
print(dad. _childclass)







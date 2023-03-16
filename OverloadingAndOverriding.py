
class Dad():            # inheritance ..dad class  inherited from human (abstract class)..so we need to 
                        #define or implement all abstract methods present in human class
    def __init__(self) -> None:     #as soon as object gets created and before assigne to object variable 
                                    #in left side.
        print("dad init")

    def speak(self):            #abstract method
        print("speak Hindi")

    def walk(self):           #abstract method
        print("fast Walk")

    def hobby (self):           #class method
        print("dad newspaper")

dad = Dad() #can not create object of class if we dont have implementation of abstract method
            #in dad class. #can't instantiate abstract class dad with abstract method speak,walk.

dad.walk()      #fast walk
dad.speak()     #speak hindi
dad.hobby()     #dad newspaper



class Beta(Dad):
    def __init__(self) -> None:
        super().__init__()
        print("Beta init")

    def hobby(self):            #method overriding,same method name in base class and child class
        print("mobile,instagram,game")

    def khilone(self):      #can not execute
        print("cycle")


    def khilone(self,a = 10):    # method overloading,same method name in same class,inheritance is not required/optional
        print("bike")

    
dad = Dad()         #dad init
dad.hobby()         #dad newspaper

beta = Beta()       #beta init
beta.speak()        #inherited from base class speak hindi
beta.hobby()        #mobile,instagream,game
beta.khilone()      #bike
beta.khilone(10)    #bike


##method overloading is not allowed in python,it  dosent support it.
#if you really want  you can use default parameter to achieve method overliading



 

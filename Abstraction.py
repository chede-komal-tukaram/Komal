from abc import ABC, abstractmethod

## we are creating Human class as abstract class
class Human (ABC):    #ABC is base class and Human is chuld class ,Helper class that provide a standers way to
                        #to create an abstraction using inheritance.
    def __init__(self) -> None:     #as soon as object gets created and before assign to object variable in
                                    #left side.
        print("Human init")

        @abstractmethod         #abstracmethod
        def speak(self):
            pass

        @abstractmethod         #@is decorater :- give special meaning to ,method
        def walk(self):
            pass

        def hobby(self):
            print("Hobby Human")




class dad(Human):
    def __init__(self) -> None:
        print("dad init")

    def speak(self):            #abstract method
        print("speak Hindi")

    def walk(self):           #abstract method
        print("fast Walk")

    def hobby (self):           #class method
        print("dad hobby")

dad = dad()              #can not create object of class if we dont have implementation of abstract method
                            #in dad class. #can't instantiate abstract class dad with abstract method speak,walk.

dad.walk()
dad.speak()
dad.hobby()



class mom(Human):
    def __init__(self) -> None:
        super().__init__()      #Human init  #super is point to base class which is Human.

        print("mom Init")       #mom init

    def speak(self):            #abstractmethod
        print("Speak Hindi")

    def walk(self):             #abstractmethod
        print("slow walk")

mom = mom()     # can not create object of class if we don't have implementation of abstract method in dad class
                #class # can't instantiate abstract class dad with abstract method speak,walk.

mom.walk()
mom.speak()
# mom.hobby()

human = Human()
# type Error : cna't instantiate abstract class Human with abstract method speak,walk.

#we can not create object of abstract class...means class have atleat one abstract method.
## Abstract class is basically meant for inheritance and contract
#abstract class can have abstract + non abstract method
# Every inheriting class of abstract class has to provide implimentation for abstract method 
#otherwise class will be incompleate.
#and we can not create object of that class.

## when to use class?
#3 when we want to share common logic across inheriting class along with shareb some contract or standers.

#we can have contractor inside abstract class however we can not create object to instantiate attribute of abstract
#class.



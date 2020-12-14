#oops
#everything is object - int, float, str, bool, functions etc
#no interface
#supports multiple inheritance, polymorphism
#supports abstract class,

#file name should not be same as class name
#file is called module and it conatins multiple functions

#empty class
class Book:
    pass #required for empty class

#instance or object
book1 = Book() #no new keyword
book2 = Book()

print(book1)
#####################
#constructor
#no constructor overloading and method overloading - use default paramerts
class Book:
    def __init__(self, name): #constructor - self is mandatory to create instance
        #self.name ="default value" #class variable - hard coded
        self.name = name

    def instance_method(self): #self is mandatory to create instance
        print("instance method")

#to-string methods
    def __repr__(self): #representation of object
        return repr(self.name)
    #def __str__(self):

book1 = Book("Mastering Python")
book1.instance_method()

print(book1)
#####################

#exercise -1 - add argument copies
class Book:
    def __init__( self,name, copies): #constructor
        #self.name ="default value" #class variable - hard coded
        self.name = name
        self.copies = copies

#to-string methods
    def __repr__(self): #accepts single param, add tuple for multiple param
        return repr((self.name, self.copies))

book1 = Book("Mastering Python", 200)

print(book1)

###############
#add attributes to object at runtime
class planet:
    pass

earth = planet()

##dynamically add attributes at runtime, no need to declare it before
earth.name = "Earth"
earth.speed = 100000
print(earth.name)
print(earth.speed)
#AttributeError: 'planet' object has no attribute 'mars'
#print(earth.mars)
print(earth) #returns object

#style guide for python
#https://www.python.org/dev/peps/pep-0008/

#zen of python
#https://www.python.org/dev/peps/pep-0020/

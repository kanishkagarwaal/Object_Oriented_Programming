# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:38:05 2018

@author: kanagarw
"""
#objects have attributes and methods
#classes are factories that create objects. Blue prints 
#class names follow camel casing


class NameOfClass():
    
    def __init__(self, param1, param2):
        self.param1=param1
        self.param2=param2
        
    def some_method(self):
        print(self.param2)

""""""        

class Sample():
    pass

obj1 = Sample()

""""""

class Dog():
    #class object attribute
    #same for any instance of he class
    #doesn't need the self keyword
    species='mammal'
    
    #init is a constructore for the class, called automatically when an instance is created
    #self is refering to the instance of the object itself
    
    # parameters
    def __init__(self,breed,name,spots):
        # user defined attributes
        # we take in the argument(above)
        # we assign it using self.attribute_name
        # by convention parameter name and attribute name are the same
        self.breed=breed
        self.name=name
        #expect boolean True/False
        self.spots=spots
        
dog1=Dog('Dalmation','Poopsie',True)    
dog2=Dog(breed='huskie',name='Plus',spots=False)    

dog3=dog1=Dog('chihuaua','chichi',False)  

"""Methods"""
# methods are basically functions inside the class
# operations/actions ---> Methods


class Dog():
    #class object attribute
    #same for any instance of he class
    #doesn't need the self keyword
    species='mammal'
    
    #init is a constructore for the class, called automatically when an instance is created
    #self is refering to the instance of the object itself
    
    # parameters
    def __init__(self,breed,name,spots):
        # user defined attributes
        # we take in the argument(above)
        # we assign it using self.attribute_name
        # by convention parameter name and attribute name are the same
        self.breed=breed
        self.name=name
        #expect boolean True/False
        self.spots=spots
    
    #use lower case to name methods
    def bark(self,number):
        print('Woof!. My name is {} and the number on my collar is {}'.format(self.name,number))

my_dog=Dog('Labrador','Plus',False)
#() to excecute the class method, unlike the attributes which need no ()

my_dog.bark(14)

"""Another example"""
class Circle():
    #class object attribute
    pi=3.14 
    
    def __init__(self,radius=1):
        self.radius=radius
        #not all attributes have to be passed as arguments
        self.area=radius*radius*self.pi
        #class object attributes can also be accessed as Circle.pi instead of self.pi
    
    def get_circumference(self):
        return self.radius * self.pi * 2
c1= Circle()  
c1.radius  
c1.get_circumference()
c2=Circle(30)
c2.get_circumference()

c2.area

"""Inheritance and polymorphism"""

class Animal():
    
    def __init__(self):
        print ('Animal created.')
    def who_am_i(self):
        print ('I am an animal.')
    def eat(self):
        print('I am eating.')
        
        
a1=Animal()
a1.eat()
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ('Dog created')
    
    #re-define some methods
    def who_am_i(self):
        Animal.who_am_i(self)
        print ('And I am a dog')
        
    def bark(self):
        print ('Woof!')

mydog=Dog()

mydog.eat()
mydog.who_am_i()
    
""""""
#super keyword
class SimpleClass:
    def __init__(self):
        print('Hello')
    def yell(self):
        print('YELLING')

l=SimpleClass()

l.yell()

class Inherited(SimpleClass):
    def __init__(self):
        print ("how are you?")
        
m=Inherited()
m.yell()

class Inherited(SimpleClass):
    def __init__(self):
        super().__init__() 
        print ("how are you?")

m=Inherited()
m.yell()
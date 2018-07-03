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



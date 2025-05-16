#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def bark(self): 
        print("Woof!") #Instance method definition
    def sit(self):
        print("The dog is sitting.")    
    
fido = Dog() # Create an instance of the Dog class
fido.bark() # Call the bark method on the instance
fido.sit() # Call the sit method on the instance

snoopy = Dog() # Create another instance of the Dog class
snoopy.bark() # Call the bark method on the second instance
snoopy.sit() # Call the sit method on the second instance
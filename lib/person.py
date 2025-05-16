#!/usr/bin/env python3

class Person:
   def talk(self):
      print("Hello World!") #Instance method definition
    
   def walk(self):
        print("The person is walking.")

greeting = Person() # Create an instance of the Person class
greeting.talk() # Call the talk method on the instance
walking = Person() # Create another instance of the Person class
walking.walk() # Call the walk method on the second instance          
#!/usr/env/python3

mylist= [1,2,3,4,5]
name= input("What is your name? ")
name= name.capitalize()

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!
print("Hi " +  name +"! Welcome to Day " +  str(mylist[1]) + " of Python Training!")

print(f"Hi {name}! Welcome to Day {mylist[1]} of Python Training!")

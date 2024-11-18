# variables - a reference (a name), a selection of memory (memory location)
# location is protected - only delete/modified/accessed by its name. 

#x = 30
#person_one_age = 30 snake-case
#personOneAge = 30 camel-case

# naming convention - be descriptive, lowercase, never start with a number. 
# be consistent
# pep-8 style guide. 


# 1var = dont start with a number
# Var = "hello" - capital is for class names!
# print = 55 dont use keywords
# VAR = constant - Var should not be changed!!

# Scope

#global_var = "accessible everywhere"

#def my_function():
 #   local_var = "accessible only inside this function"
 #   print(local_var) # this will work
 #   print(global_var) # this will also work

#my_function()

#print(local_var)

# in-built functions

# input() promtps for user input from standard input. 
# type() -- see the data type. 
# print -- prints to standard output. 

# hijacking print. 
#import sys

#with open("output.txt", "w") as file:
#    sys.stdout = file
#    print("Go to the file please!")

#sys.stdout = sys.__stdout__
#print("back to the CLI!!")

# simple data types
# int x = 10
# float x = 10.5
# bool = true/false -- 1+ or 0. something or nothing. 
# strings x = "a string a text" 

# escape chars

# \\ backslash, \n new line. \t tab, \u unicode, \U extedned unicode

# print("Person1: \they how are you?\nPerson2: \tim good thanks! \U0001f604")

# bodmas

# brackets
# order of
# division
# multiplication
# addition
# subtraction

# + - * /
# floor division // 10//3 = 3
# modulo % 10%3 = 1 

# string concatination

#name = input("What is your name? ").upper()
#age = int(input("what is your age? "))

#message = "your name is {}, your age is {}".format(name, age)
#print("your name is " + name)
#print(f"your name is {name}, your age is {age}")

# string methods

#print("hElLo WoRlD".lower())     #obj.method
#print("hello world".upper())
#print("hello world".count("l", 3, -3))
#print("hello world world world".replace("world", "class", 2))
#print("hello world".split(" "))
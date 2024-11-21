# modules

# libraries - such as the standard library. Can contain multiple packages and modules.
# packages - directories of modules
# modules - just python files. 

# many built in, some held in memory, others need to be imported and others 
# we can install. 

# pypi.org

#import math

#number = 10

#answer = math.sqrt(number) # modulename.method

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())


# import just with desired objects

#from math import pi, ceil, floor
#from random import randint

#def random_pi():
#    return floor(randint(1,10) * pi)

#for i in range(5):
#    print(random_pi())



# files
# important
# logs
# stroing and retrieving data
# sharing data
# configs
# running scripts

# most files types are supported including audio + visual.
# read, write, edit(overwrite) files.

# let focus on txt files.

# read mode ("r") - default mode - used for reading data from a file. 
# write mode ("w") - opens a file for editing, creates if does not exist. 
# append mode ("a") - opens for writing, will create a file, appends to the end. 

#eg:

#file = open("filename.txt", "mode")
#... remember to close:
#file.close()

# reading from a file:
# read() - read the entire file
# readline() - read a line and moves on to the next
# readlines() - reads all lines and puts them in a list
# seek() - go to a line or defualt to begining. 


# writing to file
# write() - write a string to the file
# writelines() - used to write a list to a file. 

#file = open("lines.txt", "r")
#lines = file.readlines()
#print(lines)

#file = open("lines-new.txt", "w")

#for n in range(1,11):
 #   newline = "this is a new line" + " " + str(n) + "\n"
 #   file.write(newline)

#file.close()

#file = open("lines-new.txt", "r")

#outfile = ""

#for line in range(1,10):
  #  if line % 2 == 0:
  #      outfile += file.readline()
 #   else:
 #       file.readline()

#file = open("lines-new.txt", "w")

#file.write(outfile)
#file.close()

# prefered syntax

#with open("lines.txt", "mode") as file:
#    for n in rangge(1,10):
#        newline = .......
#        file.write(newline)
#        # we dont need to close the file!! 
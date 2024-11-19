# iteration is another word for loops
# repeating blocks of code over and over.
# saves time avoids code duplication. 

# 2 types of loops - while + for

# while loops
# a while loop continously executes code until a condition is met.
# if no condition is met the while loop will never stop.
# we need conditions for it to start - otherwise it wont. 

#x = 0 
#while x < 101:
#    print(x)
#    x =  x + 1 

# break

#i = 0
#while i < 6:
 #   print(i)
 #   if i == 3:
 #       break
 #   i += 1

# continue

#i = 0

#while i < 6:
#    i += 1
#    if i == 3:
#        continue # continue to next step of iteration
#    print(i)

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else: 
#        print(f"hello {name}")

# for loops
# a for loop will iterate over any collection - lists/strings/dicts

# lists

#my_fruits = ["apple", "pear", "orange"]

# for item in iterable:

#for x in my_fruits:
 #   print(x)

#numbers = [1, 2, 3, 4]

#for number in numbers:
#    print(number)

# in a while loop:

#l = 0
#while l < len(numbers):
#    print(numbers[l])
#    l += 1

# range

#for a in range(5):
#    print(a)

#for a in range(1, 4):
#    print(a)

#for a in range(1, 10, 2):
#    print(a)

# strings

for letter in "hello":
    print(letter)

for word in "hello world".split():
    print(word)

# list comprehension


        #expression   # item      # iterable
#result = [x**2         for x      in range(5)]
#print(result)

#results = []
#for x in range(5):
#    results.append(x**2)

#print(results)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                       #expression    # item      # iterable   #condition
#even_numbers_squared = [number**2     for number  in numbers   if number % 2 == 0]

#print(even_numbers_squared)

# dictionaries

#for i in {"drink": "water"}:
#    print(i)

#for i in {"drink": "water"}.values():
#    print(i)

#for i in {"drink": "water"}.items():
#    print(i)

# nested loops

#for i in range(1,3):
#    for j in range(1,4):
#        print(i, "x", j, "=", i*j)


# write a loop that takes 5 names as user input and prints the name + "is cool"

# while loops
# for loop
# list comp
# optional - one line list comp (includes the printing)

# while loop

#counter = 0
#while counter < 5:
 #   name = input("enter a name: ")
 #   print(name + " is cool")
 #   counter += 1

# for loop
    
#for x in range(5):
    #name = input("name: ")
    #print(name + " is cool")

# list comp sol 1

names = [input("enter a name") for name in range(5)]
for name in names:
    print(f"{name} is cool")


# List comps are just for making lists 

# combined list comp

# inner list 
#[input("enter a name") for x in range(5)]
# outer list
#[print(f"{name} is cool") for names in iterable]


x = [print(f"{name} is cool") for names in [input("enter a name") for x in range(5)]]

# list comp side affect
print(x)

# a function either perfomrs a task or returns a value.
# repeatability. 

#def greet(name): # define parameters to take arguments
 #   print(f"hello {name}")

#greet("chris")

#def greet1(first_name, last_name, age):
#        print(f"{first_name} {last_name} is {age}")

#greet1("john", "smith", 10)

# print and input shouldnt be inside functions
# limits the reusibility of the code. 
# Use return and store in a variable. 


#def greeter(name):
#    return f"hello {name}"

#x = greeter("chris")

#print(x)

# default values

#def greet3(name, age=10):
#    return f"{name} is {age}"

#print(greet3("chris"))
#print(greet3("chris", age=20))


# *args
# if we do not know how many args will be passed through
# receives a tuple of args.

#def fruit_list(*fruits):
 #   print("The list of fruits is: ")
 #   for fruit in fruits:
 ##       print(fruit)

#fruit_list("orange", "pear", "kiwi")

#def make_pizza(size, *toppings):
   # print(f"order for {size}-inch pizza with the following toppings:")
  #  for topping in toppings:
 #       print(topping)

#make_pizza(10, "peppers", "mushrooms", "")

# kwargs 
# order doesnt/shouldnt matter
# send args as key:value pairs

#def fruit_list(fruit1, fruit2, fruit3):
#    print(f"fruit 1 is {fruit1}")
#    print(f"fruit 2 is {fruit2}")
#    print(f"fruit 3 is {fruit3}")

#fruit_list(fruit3="apple", fruit1="pear", fruit2="orange")

# **kwargs
# if we dont know how many key value pairs will be passed through. 

#def fav_food(**food):
#    print(f"fav food is", food['dessert'], "not", food['dairy'])

#fav_food(dessert="ice-cream", fruit="apple", dairy="milk")

# combined *args and ** kwargs
#def combine(*args, **kwargs):
#    print("args: ", args)
#    print("kwargs: ", kwargs)

#combine(1, 2, 3, a=5, b=10)

# / is a positional marker
# introduced in python 3.6/3.8
# before / is positional args only and is enforced
# after is keywords but not enforced. 

#def example(a, b, /, c, d):
#    print(f"a = {a}, b = {b}, c = {c}, d = {d}")
#example("a", "b", "c", d="d")

#def maths_operation(a, b, /, operation="add", *, decimal_place=4):
    #if operation == "add":
    #    result = a + b
    #elif operation == "subtract":
    #    result = a - b
   # else:
  #      raise ValueError("invalid operation")
 #   return round(result, decimal_place)

#print(maths_operation(10, 5))
#print(maths_operation(10, 5, "subtract", 10))
#print(maths_operation(10.255, 5.255, decimal_place=2))

# recurrsion 

#def factorial(n):
   # if n == 1:
  #      return 1
 #   else:
 #       return n * factorial(n - 1)

#print(factorial(5))

# lambda functions
# short unnamed functions, calculates a single expression.
# lambda argument: expression (iterable)

#def add(x, y):
#    return x + y

#add_lambda = lambda x, y: x + y

#print(add(5 ,5))
#print(add_lambda(2, 4))

#numbers = [1, 2, 3, 4]

#squared = map(lambda x: x**2, numbers)

#print(list(squared))    

# higher order functions
# Either takes in a function as an arg or returns a function

#def square(x):
#    return x * x

#def apply_function(func, value):
#    return func(value)

#print(apply_function(square, 5))

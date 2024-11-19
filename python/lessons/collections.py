# collections are our complex data types.
# store data. 

# Lists - ordered(indexed), mutable, collection of values -
# [a(index postition 0), b(index position 1)....]

# dictionaries - unordered(not indexed), mutable, collection of key:value pairs.
# { key: value, key1: value, key2: value...} 

# tuples - ordered, immutable.
# () or no brackets. eg: x = 1, 2, 3 - y = (1, 2, 3)

# sets - unordered, mutable, collection of unique values. 
# {a, b, c} 

# lists

#food = ["rice", "pasta", "bread", "apple"]

#print(food)

# direct access

#print(food[0])
#print(food[3])
#print(food[-2])

# slicing, second number is up to but not including. 

#print(food[0:2])
#print(food[0: ])

# altering with direct access

#food = ["rice", "pasta", "bread", "apple"]

#food[0] = "pizza"
#print(food)

#del food[1]
#print(food)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# stings methods

# append

#my_fruits = ["apple", "pear", "kiwi"]

#my_fruits.append("orange")

#print(my_fruits)

#my_fruits.remove("apple")
#print(my_fruits)

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "grapes")
#print(my_fruits)

#my_fruits.extend(["melon", "blueberries"])

#print(my_fruits)


# sort
my_fruits = ["apple", "pear", "kiwi"]

#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = "#".join(my_fruits)
#print(x)

# dictionaires

#drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcoholic": "wine"}

#print(drinks)

# direct access 

#print(drinks["still"])

#drinks["non-alcoholic"] = "water"
#print(drinks)

#drinks["non-alcoholic"] = "squash"
#print(drinks)

# methods 

# valuus/keys/items

#print(drinks.values())
#print(drinks.keys())
#print(drinks.items())

# get method
#print(drinks.get("still"))
#print(drinks.get("stilleeee"))
#print(drinks.get("stilllleeeee", "some string"))

# exercise: 

# make a dictionary of authors and books. (3 authors a least 2 books each)
# have an input that asks for author name.
# print a STRING of books by that author (NOT A LIST).... (use .join)
# Have a little bit error handling for incorrect names using a method.  

#books = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

# solution 1

#x = input("Enter an author name: ")

#print(", ".join(books[x]))

# solution 2

#y = input("Enter an author name: ")

#x = books.get(y, [])

#print(", ".join(x) or "author not found")

# tuples
# can use min, max, len, zip. 

# slight less memory and slightly faster to run
# signifies we dont want the data to change!

# rectangle = 10, 5 # or (10 , 5)
# rectangle[0] = 15

# sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))


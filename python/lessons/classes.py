# classes are part of OOP.
# # 4 principles of OOP:
# encapsulation - privacy 
# Polymorphism - different ways of implementing methods(functions).  
# Inheritance - inheriting from parent classes. 
# abstaraction - i want to implement but not see the code. 
# Well structured code, readabilty, code safety, good for refacrotring. 

# class - a blueprint - attributes (vars/args/methods)
# object - an instance of the class.  
# can make many objects of the same type. 

#class Dog:
  #  energy = "high" # class attribute

 #   def speak(self):    # a method
 #       print("bark")

#fido = Dog() # initialises the object of the class Dog

#fido.speak()
#print(fido.energy)

#fido.energy = "low"
#print(fido.energy)

#class Student:
#    pass

#student1 = Student()
#student2 = Student()

#student1.first = "John"
#student1.last = "smith"
#student1.age = 10

#print(student1.age)

#class Student:
 #   def __init__(self, first, last, age): # init method (dunder - background task)
 #       self.first = first # init initialsises the object with these params.
 #       self.last = last # the self param refers to the object itself
 #       self.age = age # self. -- maps the params/args to the object. 
        

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)

#print(student1.age, student2.first)

#class Student:
  #  def __init__(self, first, last, age): # init method (dunder - background task)
  #      self.first = first # init initialsises the object with these params.
  #      self.last = last # the self param refers to the object itself
 #       self.age = age # self. -- maps the params/args to the object. 
 #       self.full = first + " " + last
        

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)

#print(student1.full, student2.full)

#class Student:
    #def __init__(self, first, last, age): # init method (dunder - background task)
    #    self.first = first # init initialsises the object with these params.
   #     self.last = last # the self param refers to the object itself
  #      self.age = age # self. -- maps the params/args to the object. 
        #self.full = first + " " + last

 #   def fullname(self):
 #       return self.first + " " + self.last
        

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)

#print(student1.fullname())
#print(Student.fullname(student2))

# change an attribute with a method

#class Student:
    #def __init__(self, first, last, age): # init method (dunder - background task)
   #     self.first = first # init initialsises the object with these params.
   #     self.last = last # the self param refers to the object itself
   #     self.age = age # self. -- maps the params/args to the object. 
        #self.full = first + " " + last

  #  def fullname(self):
  #      return self.first + " " + self.last

 #   def change_age(self):
 #       self.age = self.age + 1 
        

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)

#print(student1.age)
#student1.change_age()
#print(student1.age)

# self-class variable

#class Student:

    #age_increase_amount = 25

   # def __init__(self, first, last, age): # init method (dunder - background task)
   #     self.first = first # init initialsises the object with these params.
   #     self.last = last # the self param refers to the object itself
   #     self.age = age # self. -- maps the params/args to the object. 
        #self.full = first + " " + last

  #  def fullname(self):
  #      return self.first + " " + self.last

 #   def change_age(self):
 #       self.age = self.age + self.age_increase_amount
        

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)

#print(student1.age)
#student1.change_age()
#print(student1.age)

#print(student1.age_increase_amount)

# Dict

#print(student1.__dict__)
#print(student2.__dict__)
#print(Student.__dict__)

# object changes class var.

#student1.age_increase_amount = 20
#student1.change_age()

#print(student1.age)
#print(student1.__dict__)
#print(student2.__dict__)

# non self class vars

#class Student:

    #age_increase_amount = 25
    #__num_of_students = 0

    #def __init__(self, first, last, age): # init method (dunder - background task)
        #self.first = first # init initialsises the object with these params.
      #  self.last = last # the self param refers to the object itself
       # self.age = age # self. -- maps the params/args to the object. 
        #self.full = first + " " + last

     #   Student.__num_of_students += 1 

    #def fullname(self):
     #   return self.first + " " + self.last

    #def change_age(self):
   #     self.age = self.age + self.age_increase_amount

  #  @classmethod
 #   def getNumOfStudents(cls):
 #       return cls.__num_of_students
        

#print(Student.num_of_students)
#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "Smith", 12)
#print(Student.num_of_students)
#print(Student.getNumOfStudents())
#print(Student.getNumOfStudents(cls=Student))

# inheritance

#class Animal:
   # def __init__(self, name, species):
   #     self.name = name
  #      self.species = species

 #   def eat(self):
 #       print(f"{self.name} is eating")

#class Cat(Animal):
  #  def __init__(self, name, species, breed):
  #      super().__init__(name, species)
  #      self.breed = breed

 #   def meow(self):
 #       print("meow")


#my_cat = Cat("w", "x", "y")

#my_cat.eat()
#my_cat.meow()

# __str__ method 


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"


class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
            return super().__str__() + f" {self.breed}"


my_cat = Cat("w", "x", "y")

my_cat.eat()
my_cat.meow()
print(my_cat)


#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

# RPS - as a class (self-contained)

# optional:

# Harder challenge (stretch goal): 

#Create a Book class and BookShelf class that can be used to manage a collection of books. 
#Create a Book class that has the following attributes: 
#title (str), author (str), publisher (str), publication year (int). 
#The class should also have a str method that returns the book's information in a 
#formatted string. 
#Create a BookShelf class that has the following attributes: 
#capacity (int), list of books (list). 
#The class should have the following methods: 
#- add_book: adds a book to the list of books if the shelf is not full 
#- remove_book: removes a book from the list of books if it exists on the shelf 
#- find_book_by_title: searches for a book by its title 
#and returns the book object if found 
#- find_books_by_author: searches for books by a specific author 
#and returns a list of book objects if found 
#The class should also have a str method that returns a string representation 
#of the books on the shelf. 

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.
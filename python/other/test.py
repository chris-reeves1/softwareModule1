class Book:
    def __init__(self, title, author, publisher, pubYear):
        self.title = str(title)
        self.author = str(author)
        self.publisher = str(publisher)
        self.pubYear = int(pubYear)

    def __str__(self):
        return(f"{self.title} - {self.author} - {self.publisher} - {self.pubYear}")

class BookShelf:
    def __init__(self, capacity, booksList):
        self.capacity = int(capacity)
        self.booksList = booksList

    def __str__(self):
        return(f"{self.booksList}")
    
    def AddBook(self, newBook):
        if len(self.booksList) < self.capacity:
            self.booksList.push(f"{newBook}")
            return(f"{newBook} has been shelved successfully!")
        else:
            return(f"{newBook} could not be shelved, free up space.")
        
    def RemoveBook(self, book):
        found = False
        while found == False:
            for i in range(len(self.booksList)):
                if self.booksList[i] == book:
                    self.booksList[i].pop()
                    found = True
                    return(f"{book} was removed successfully.")
            if found == False:
                return(f"{book} could not be removed as it is not on this shelf.")
    
    def FindBookByTitle(self, book):
        for i in range(len(self.booksList)):
            if self.booksList[i] == book:
                found = True
                return(book.__str__(book))
        if found == False:
            return(f"{book} could not be removed as it is not on this shelf.")
                    
    def FindBookByAuthor(self, author):
        NEWLIST = []
        for i in range(len(self.booksList)):
            if self.booksList[i] == self.author:
                found = True
                NEWLIST.push(self.booksList[i])
        if found == False:
            return(f"{author} could not be found as it is not on this shelf.")
        else:
            return(NEWLIST)
        

book1 = Book("Casino Royale" , "Fleming" , "publisher1" , 1951)
book2 = Book("Goldfinger" , "Fleming" , "publisher1" , 1960)
book3 = Book("Philosopher's Stone" , "Rowling" , "publisher2" , 1991)
book4 = Book("Storyteller" , "Grohl" , "publisher3" , 2021)

myBookshelf = BookShelf(3 , [])

print( myBookshelf.AddBook(book1) )
print( myBookshelf.AddBook(book4) )
print( myBookshelf.RemoveBook(book1) )
print( myBookshelf.FindBookByTitle("Storyteller"))

myBookshelf.RemoveBook(book4)

myBookshelf.addBook(book1)
myBookshelf.AddBook(book2)

print( myBookshelf.FindBookByAuthor("Rowling") )



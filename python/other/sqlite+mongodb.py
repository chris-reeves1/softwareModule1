import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

# commands
#CREATE TABLE	Create a new table.
#INSERT INTO	Insert new data into a table.
#SELECT	Query data from a table.
#UPDATE	Modify existing data.
#DELETE	Remove data from a table.
#WHERE	Filter rows based on a condition.


# create table
c.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT)
    """)

conn.commit() # saves changes

# insert data into table

c.execute("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
""", ("alice", 20, "A"))
conn.commit()


# Query data
c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)

# update data
c.execute("""
    UPDATE students
    SET grade = ?
    WHERE name = ?
""", ("B", "alice"))
conn.commit()

# Delete data
c.execute("""
    DELETE FROM students
    WHERE name = ?
""", ("alice",))
conn.commit()

# Exercise: SQLite Database
#Create a small database for a library system.
# Create a Table:
# books: Columns - id, title, author, year_published, available.
# Insert Data:
# Add at least 3 books to the database.
# Query Data:
# List all books in the library.
# Filter books by a specific author.
# Update Data:
# Mark a book as unavailable.
# Delete Data:
# Remove a book from the library.

import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 1: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year_published INTEGER,
    available BOOLEAN
)
""")
conn.commit()

# Step 2: Insert Data
books = [
    ("Book A", "Author 1", 2000, True),
    ("Book B", "Author 2", 2010, True),
    ("Book C", "Author 1", 2015, False)
]
cursor.executemany("""
INSERT INTO books (title, author, year_published, available)
VALUES (?, ?, ?, ?)
""", books)
conn.commit()

# Step 3: Query Data
print("All books:")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

print("\nBooks by Author 1:")
cursor.execute("SELECT * FROM books WHERE author = ?", ("Author 1",))
for row in cursor.fetchall():
    print(row)

# Step 4: Update Data
cursor.execute("""
UPDATE books
SET available = ?
WHERE title = ?
""", (False, "Book B"))
conn.commit()

# Step 5: Delete Data
cursor.execute("DELETE FROM books WHERE title = ?", ("Book A",))
conn.commit()

# Final List of Books
print("\nFinal books:")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()


###################################
###################################
###################################

# set-up on Ununtu:
# curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
# echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
# sudo apt update
#  didnt work so...
# echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
# sudo apt update
# install pip if needed: sudo apt install python3-pip
# probably: sudo apt install python3-pymongo

from pymongo import MongoClient

# Connect to MongoDB - creates if not exist.
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]  # Database
collection = db["students"]  # Collection - like a table for grouped data --
# doesnt enforce schema!!!! 
# collection for users, products, orders etc would make sense. 

# Insert Data
collection.insert_many([
    {"name": "Alice", "age": 25, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B",},
    {"name": "Charlie", "age": 30, "grade": "C"}
])

# Query Data
print("All Students:")
for student in collection.find():
    print(student)

# Update Data
collection.update_one({"name": "Alice"}, {"$set": {"grade": "A+"}})
collection.update_one({"name": "Alice"}, {"$set": {"pathway": "jenkins"}})
# add ne wfield to all documents in collection:
# collection.update_many({}, {"$set": {"pathway": "default_pathway"}})


# Query After Update
print("\nUpdated Student:")
print(collection.find_one({"name": "Alice"}))

# Delete Data
collection.delete_one({"name": "Charlie"})

# Query After Deletion
print("\nRemaining Students:")
for student in collection.find():
    print(student)

db["students"].drop()



#Operator	Description	Example
#$gt	Greater than	{"age": {"$gt": 30}}
#$lt	Less than	{"age": {"$lt": 25}}
#$in	Matches any value in a list	{"name": {"$in": ["Alice"]}}
#$set	Sets a field to a specified value	{"$set": {"age": 26}}
#$unset	Removes a field from a document	{"$unset": {"age": ""}}
#$exists	Checks if a field exists	{"age": {"$exists": true}}
#$push	Appends a value to an array	{"$push": {"skills": "SQL"}}
#$pull	Removes a value from an array	{"$pull": {"skills": "SQL"}}
#$group	Groups documents for aggregation	{"$group": {"_id": "$grade"}}


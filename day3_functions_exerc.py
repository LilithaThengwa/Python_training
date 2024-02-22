library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

# Task 1
# Add Book Function: Write a function add_book(library, new_book) that adds a new book to the library.
# add_book library new_book


# def addbook(newbook, library):
#   title = input("Enter title: ")
#   author = input("Enter author: ")
#   year = int(input("Enter year: "))
#   available = True
#   newbook = {"title": title, "author": author, "year": year, "available" : available}
#   library.append(newbook)
#   return library

# newbook = {}
# print(addbook(newbook, library))

# Task 2 
# Search Books by Author Function: Write a function search_by_author(library, author_name) that returns a list of books by a specific author.

# result = [   
#   {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},  
#   {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False}
# ]

def search_by_author(library, author_name):
  booksbyauthor = []
  for book in library:
    if book["author"] == author_name:
       booksbyauthor.append(book)
       return booksbyauthor

    else:
     print("No books by this author")

print(search_by_author(library, "Mark Lutz"))


def check_out_book
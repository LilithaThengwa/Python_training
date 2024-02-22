library_list = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

# Task 1

# def addbook(newbook, library):
#   title = input("Enter title: ")
#   author = input("Enter author: ")
#   year = int(input("Enter year: "))
#   available = True
#   newbook = {"title": title, "author": author, "year": year, "available" : available}
#   library.append(newbook)

# newbook = {}
# print(addbook(newbook, library_list))

#=========================================================

# Task 2 
# Search Books by Author Function: Write a function search_by_author(library, author_name) that returns a list of books by a specific author.

# def search_by_author(library, author_name):
#     return [book for book in library if book["author"] == author_name]

# print(search_by_author(library_list, "Mark Lutz"))

#=========================================================

# Task 3
def check_out_book(library, title):
    for book in library:
        if book["title"] == title and book["available"]:
            book["available"] = False
            return f"{title} has been checked out."
    return "Book not found or already checked out"

print(check_out_book(library_list, "Fluent Python"))

#=========================================================
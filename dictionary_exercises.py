# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]

# diction = []

# for dict in books:
#   diction.append(dict)
# # print(dicts)

# for book in diction:
#     if book["rating"] >= 4.7:
#       print(book["title"])

# rated = [book["title"] for book in books if 
# book["rating"] >= 4.7] #with list comprehension
#sorted_rated = sorted(rated)#sortted
# print(rated)

#==============================================================

# task1

inventory = [

  {"name": "Apple", "quantity": 30, "price": 0.50},

  {"name": "Banana", "quantity": 20, "price": 0.20}

]

# prod_name = input("Enter product name: ")
# quantity = int(input("Enter quantity: "))
# price = float(input("Enter price: "))
# product = {"name": prod_name, "quantity": quantity, "price": price} 
# inventory.append(product)

# print(inventory)

#==============================================================

# prod_name = "orange"
# quantity = 10
# price = 0.30

# new_product = {"name": prod_name, "quantity": quantity, "price": price} 
 
# for item in inventory:
#   if (item["name"] == prod_name):
#     item["quantity"] += quantity
#     item["price"] += price
#     break
# else:
#   inventory.append(new_product)


#==============================================================


# task

# guests = [

#   {"name": "Alice", "age": 25, "code": "VIP123"},

#   {"name": "Bob", "age": 17, "code": "VIP123"},

#   {"name": "Charlie", "age": 30, "code": "VIP123"},

#   {"name": "Dave", "age": 22, "code": "GUEST"},

#   {"name": "Eve", "age": 29, "code": "VIP123"}

# ]

# blacklist = ["Dave", "Eve"]
# PASS_CODE = "VIP123"

# guestlist = [guest["name"] for guest in guests if guest["name"] not in blacklist and guest["code"] == PASS_CODE and guest["age"] >= 21]

# print(guestlis)# filtered guest names

#==============================================================

# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

# for employee in employees: #update employee experience
#   employee["experience"] = employee.get("experience", 0) + 1

# print(employees)

# for employee in employees:# update status based on experience
#   if employee.get('experience', 0) >= 5:
#     employee['status'] = "Senior"
#   elif 3 <= employee.get('experience', 0) < 5: 
#     employee['status'] = "Mid-Level"
#   else:
#     employee['status'] = "Junior"
# print(employees)

#==============================================================

# # Copying and merging dictionaries with unpacking
# movie = {
#   "name": "Mr Bones",
#   "year": 2001
# }

# detail = {"actor": "Leon Schuster", "Director": "Gray Hofmeyr"}

# movie_detail = {**movie, **detail} #merging dictionaries
#print(movie_detail)

# # Make copy of dicitonary
# movie_copy1 = movie.copy()

# # Unpacking Operator * -> List | ** -> Dictionaries
# movie_copy2 = {**movie, "rating": 10}
# print(movie_copy2)

# movie_copy3 = {**movie, "rating":10, "year": 2002} # last "year" overrides previous one
# print(movie_copy3)

# movie_copy4 = {"rating":10, "year": 2002, **movie} # last "year" overrides previous one
# # the unpacking is like this
# # {"rating": 10, "year":2002, "name": "Mr Bones", "year":2001} (2001 overrides!)
# print(movie_copy4)

#==============================================================

# nums = [90, 50, 80]
# for idx, num in enumerate(nums):
#   print(idx, num)#prints index and number

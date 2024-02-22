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

# prod_name = input("Enter product name: ")
# list = []

# for item in inventory:
#   list.append(item["name"])

# if(prod_name in list):
#   quantity = int(input("Enter quantity: "))
#   price = float(input("Enter price: "))
#   for item in inventory:
#     item["quantity"] = item["quantity"] + quantity
#     item["price"] = item["price"] + price
    
# else:
#   quantity = int(input("Enter quantity: "))
#   price = float(input("Enter price: "))
#   product = {"name": prod_name, "quantity": quantity, "price": price} 
#   inventory.append(product)
   
# print(inventory)

# prod_name = input("Enter product name: ")

# for item in inventory:
#     if(prod_name == item["name"]):
#       quantity = int(input("Enter quantity: "))
#       price = float(input("Enter price: "))
#       item["quantity"] = item["quantity"] + quantity
#       item["price"] = price
#       break
      
# else:
#   quantity = int(input("Enter quantity: "))
#   price = float(input("Enter price: "))
#   product = {"name": prod_name, "quantity": 
#   quantity, "price": price} 
#   inventory.append(product)

# print(inventory)

# product_name = input("What is the product name? ")
# product_quantity = int(input("What is the quantity? "))
# product_price = float(input("What is the price? "))

# for product in inventory:
#   if(product["name"] == product_name):
#     product["quantity"] += product_quantity
#     product["price"] = product_price
#     break

# print(inventory)

# newname = input("What is the product name? ")
# newquantity = int(input("What is the quantity? "))
# newprice = float(input("What is the price? "))
# addproduct = True
# for product in inventory:
#   if (newname == product["name"]):
#     print(product["name"])
#     product["quantity"] += newquantity
#     product["price"] = newprice
#     addproduct = False
#     break
# if (addproduct):
#   new_product = {"name": newname, "quantitiy": newquantity, "price": newprice}
#   inventory.append(new_product)
# print(inventory)

# task

# guests = [

#   {"name": "Alice", "age": 25, "code": "VIP123"},

#   {"name": "Bob", "age": 17, "code": "VIP123"},

#   {"name": "Charlie", "age": 30, "code": "VIP123"},

#   {"name": "Dave", "age": 22, "code": "GUEST"},

#   {"name": "Eve", "age": 29, "code": "VIP123"}

# ]

# blacklist = ["Dave", "Eve"]
# guestlist = []

# for guest in guests:
#   guestlist.append(guest["name"])

# for guest in guests:
#   if guest["name"] in blacklist:
#       guestlist.remove(guest["name"])
    
#   elif guest["age"] < 18:
#       guestlist.remove(guest["name"])
    
#   elif guest["code"] != "VIP123":
#       guestlist.remove(guest["name"])
# print(guestlist)

# list = [guest ]

employees = [
  {"name": "Alex", "experience": 2},
  {"name": "Gemma"},
  {"name": "Rashay", "experience": 4},
  {"name": "Thato"}
]

# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1

# print(employees)

for employee in employees:
  if employee.get('experience', 0) < 3:
    employee['status'] = "Junior"
  elif employee.get('experience', 0) < 5: 
    employee['status'] = "Mid-Level"
  else:
    employee['status'] = "Senior"
print(employees)

# # Copy
# movie = {
#   "name": "Mr Bones",
#   "year": 2001
# }

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

# Q1. Data Sorting and Ranking

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93}
]

# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.
# sortedstudents = sorted(students, key = lambda student: student["grade"], reverse=True)
# rank = 1
# for student in sortedstudents:
#     student["rank"] = rank
#     rank += 1

# print(sortedstudents)
    
# with list comprehension

result = [student for student in sorted(students, key = lambda student: student["grade"], reverse=True)]
# print(result)

# # more efficient
# withrank = list(map(lambda student: {**student, "ranking": }, sortedstudents))
# print(withrank)

#=================================================================================================================================

# Q2. Merging Data from Two Lists

employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.

# for employee in employees:
#     for salary in salaries:
#         if (employee["id"] == salary["id"]):
#             employee.update(salary)    

# print(employees)

#list comp

[employee.update([salary for salary in salaries if (employee["id"] == salary["id"])]) for employee in employees]
# print(employees)   

#=======================================================================================================================

# Q3. Advanced Filtering with Multiple Conditions

products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400}
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

# for product in products:
#     if (product["category"] == "Electronics" and product["price"] < 500):
#         products.remove(product)

filteredproducts = list(filter(lambda product: (product["category"] == "Electronics") and (product["price"] < 500), products))

# print(filteredproducts)

# ==============================================================================================================================

# Q4. Complex Data Transformation

orders = [
    {"order_id": 1, "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}]},
    {"order_id": 2, "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}]}
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

orders_dict = {}
for order in orders:
    print(order)
    for id, val in order.items():
        print(id)
        print(val)
        # orders_dict["name"] = val["product"]
        # orders_dict["total quantity"] = val["quantity"]

# print(orders_dict)
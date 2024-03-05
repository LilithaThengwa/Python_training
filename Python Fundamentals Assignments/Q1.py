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


sortedstudents = sorted(students, key = lambda student: student["grade"], reverse=True)
for rank, student in enumerate(sortedstudents):
     student["rank"] = rank + 1
print(sortedstudents)

# # more efficient 🤔🤷🏾‍♂️
# rank = 0
# withrank = list(map(lambda student: {**student, "ranking": rank ++1}, 
#            sorted(students, key = lambda student: student["grade"], reverse=True)))
# print(withrank)

#=================================================================================================================================

# Q2. Merging Data from Two Lists

employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.

# for employee in employees:
#     for salary in salaries:
#         if (employee["id"] == salary["id"]):
#             employee.update(salary)    # ✅

# print(employees)

#list comp and unpacking opp

# [employee.update([salary for salary in salaries if (employee["id"] == salary["id"])]) for employee in employees] ❌
# print(employees)   

merged = [{**employee, "salary": salary["salary"]} for employee in employees
           for salary in salaries if employee["id"] == salary["id"]] #✅
# print(merged)

#=======================================================================================================================

# Q3. Advanced Filtering with Multiple Conditions

products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400}
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

# for product in products:
#     if (product["category"] != "Electronics" or product["price"] > 500):
#         products.remove(product) # ❌

# print(products)

# with list comp

# filteredproducts = [product for product in products if product["category"] == "Electronics" 
#                     and product["price"] < 500]

filteredproducts = list(filter(lambda product: (product["category"] == "Electronics")
                                and (product["price"] < 500), products)) 
# print(filteredproducts)

# ==============================================================================================================================

# Q4. Complex Data Transformation

orders = [
    {"order_id": 1, "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}]},
    {"order_id": 2, "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}]}
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

prod_quant = {}
for order in orders:    
    for item in order["items"]:
         prod = item["product"]
         quantity = item["quantity"]
         prod_quant[prod] = quantity
         if (prod_quant[prod] == prod):
              prod_quant[prod] = prod_quant[prod] + quantity #almost

# print(prod_quant)
                    
# ==========================================================
                    
# Q5. Data Consolidation and Summarization
                    
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"}
]
# Expected Task: Summarize the total amount spent per category.

# totalpercat = {}
# transport_amount = 0
# food_amount = 0
# for transaction in transactions:
#      if (transaction.get("category", 0) == "Food"):      
#           food_amount = food_amount + transaction["amount"]
#           totalpercat["Food"] = food_amount
#      elif (transaction.get("category", 0) == "Transport"):
#           transport_amount += transaction["amount"]
#           totalpercat["Transport"] = transport_amount
# print(totalpercat)

# better

totalpercat = {}

for transaction in transactions:
     category = transaction["category"]
     amount = transaction["amount"]
     totalpercat[category] = totalpercat.get(category, 0) + amount #if category exists, fetch and add amount. 0 is default.

# print(totalpercat)

#================================================================

# Q6. Grouping and Aggregating Data

sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100}
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.

# both work

# total_per_person = {}
# for sale in sales:
#      salesperson = sale["salesperson"]
#      amount = sale["amount"]
#      total_per_person[salesperson] = total_per_person.get(salesperson, 0) + amount
# print(total_per_person)

total_with_comp = {}
{total_with_comp.update({sale["salesperson"]: total_with_comp.get(sale["salesperson"], 0) + sale["amount"]}) for sale in sales}
# print(total_with_comp)


#====================================================================================================== 

# Q7. Lambda Functions for Spell Power

spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.

sortedspells = sorted(spells, key = lambda x: x[1], reverse=True)
# print(sortedspells)

#======================================================================================================

# Q8. Map Transformation for Potion Ingredients

ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.

withquant = list(map(lambda ingredient: ingredient + ": 3 grams", ingredients))
# print(withquant)

# =====================================================================================================================

# Q9. Magical Book Filter and Formatter

books = [{"title": "A History of Magic", "pages": 100}, {"title": "Magical Drafts and Potions", "pages": 150}]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

filtered = list(map(lambda title: title["title"].upper(), list(filter(lambda pages: pages["pages"] > 120, books))))
# print(filtered)

# ======================================================================================================================

# Q10. Wizard Duel Game Class

# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.
class WizardDuel:
     health = 100
     def __init__(self, name):
          self.name = name
          self.health = 100

     def cast(self, damage, target):
          target.health -= damage

     def lose_health(self, damage):
         self.health -= damage
         if (self.health < 0):
             self.health = 0

     def duel(self, target):
         target.cast(self, 50)
         self.cast(target, 60)
         target.cast(self, 40)
         self.cast(target, 60)

         if (self.health <= 0):
             return f"{self.name} with {self.health} points left!"
         else:
             return f"{target.name} with {target.health} points left!"

harry = WizardDuel("Harry")
draco = WizardDuel("Draco")

# print(harry.duel(draco))
          
# ===========================================================================================================================
          
# Q11. Custom Error Handling in Potion Making
          
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.
          
class PotionError(Exception):
    def __init__(self, ingredient, potion):
        self.ingredient = ingredient
        self.potion = potion
        self.message = f"Caught PotionError: '{self.ingredient}' is not a valid ingredient for the {self.potion}."
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

# list of ingredients for love potion    
def brew(ingredient, potion):
     try:
         if(ingredient.lower() == "eye of newt"):
              raise PotionError(ingredient, potion)
     except PotionError as e:
          print(e)

# brew("Eye of Newt", "Love Potion")

#=========================================================================

# Q12. Hogwarts Library Database Query

library = [{"title": "Unfogging the Future", "author": "Cassandra Vablatsky"}, {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"}]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.

bagshot_books = [book for book in library if book["author"].lower() == "bathilda bagshot"]

# print(bagshot_books)

#==============================================================================================================================================================================

# Q13. Hogwarts House Points Calculator

house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40}
]
# Expected Task: Aggregate points for each house and print the total.

# total_points = []
# total_dict = {}
# gryf_points = 0
# slyt_points = 0
# for house in house_points:
#      if (house["house"] == "Gryffindor"):
#           gryf_points += house["points"]
#      elif (house["house"] == "Slytherin"):
#           slyt_points += house["points"]
#      total_dict["Gryffindor"] = gryf_points
#      total_dict["Slytherin"] = slyt_points
# total_points.append(total_dict)
# print(total_points)

# less verbose

# total_points_list = []
# total_points = {}
# for item in house_points:
#      house = item["house"]
#      points = item["points"]
#      total_points[house] = total_points.get(house, 0) + points
# total_points_list.append(total_points)

# print(total_points_list)

# even less verbose

total_points = {}

for house in house_points:
     total_points[house["house"]] = total_points.get(house["house"], 0) + house["points"]
# print(total_points)
# ==============================================================================

# Q14. Class Inheritance for Magical Creatures

# Expected Task: Create a base class `MagicalCreature` and subclasses `
class MagicalCreature:
     def __init__(self, name):
          self.name = name

     def sound(self):
          return "Some sound"
     
class Dragon(MagicalCreature):
     def sound(self):
          return "Roar"
     
class Unicorn(MagicalCreature):
     def sound(self):
          return "Neigh"
     
generic = MagicalCreature("generic")
dragon = Dragon("dragon")
unicorn = Unicorn("unicorn")

# print(dragon.sound())

# ======================================================================================

# Q15. Custom Sorting with Lambda for Magical Artifacts

artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7}
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.

# byage = sorted(artifacts, key = lambda age: age["age"], reverse = True)
# bypower = sorted(byage, key = lambda power: power["power"], reverse = True)
final = sorted(artifacts, key = lambda both: (both["age"], both["power"]), reverse = True)
# print(bypower)
# print(final)

# =======================================================================================================

# Q16. Wizard Profile Generator with f-strings

wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.

profile = f"{wizard['name']}, the {wizard['title']} of {wizard['house']}."
# print(profile)

#=========================================================================================================================

# Q17. Magical Creature Adoption Matching

adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.

match = []
for adopter in adopters:
     for creature in creatures:
          if(adopter[1] == creature[1]):
           match.append((adopter[0], creature[0]))  

# print(match)

# matches = list(filter(lambda creature: creature[0], creatures))
# matches = list(map(lambda adopter: adopter[0], adopters))
# matchwithcreature = list(map(lambda adopter: (adopter[0], list(map(lambda creature: creature[0], filter(lambda cre: cre[1] == adopter[1], creatures))))[0]), adopters)
# withcreature = list(map(lambda adopter: adopter[1] == filter(lambda creature: creature[1], creatures), adopters))
# print(matchwithcreature)

# =======================================================================================================================================

# Q18. Advanced Potion Making with Nested Loops

ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

length = len(ingredients)
combos = []
possible_potions = []

# for ingredient_idx in range(length):
#      for other_idx in range(ingredient_idx + 1, length):
#           ingredient = ingredients[ingredient_idx]
#           other_ingredient = ingredients[other_idx]
#           combos.append(f"{ingredient} and {other_ingredient}")

# with comprehension
          
combos = [f"{ingredients[i]} and {ingredients[j]}" for i in range(length) for j in range(i + 1, length)]

for pair in combos:
    if pair == "Moonstone and Silver Dust":
      possible_potions.append(f"Combining {pair} produces an invisibility potion.")
    elif pair == "Moonstone and Dragon Blood":
      possible_potions.append(f"Combining {pair} produces a strength potion.")
    elif pair == "Silver Dust and Dragon Blood":
      possible_potions.append(f"Combining {pair} produces a speed potion.")


# print(possible_potions)

# ==============================================================================================================
                
# Q19. Nested Data Manipulation

data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]}
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.

# for dat in data:
#      for k, v in dat.items():
#           if (k == "tags" and "tag1" in v):
#                v.append("tag4")

# more concise

# for dat in data:
#     if ("tag1" in dat["tags"]):
#                dat["tags"].append("tag4")  

# with comprehension

data = [{**dat, "tags": dat["tags"] + ["tag4"]} if "tag1 " in dat["tags"] else dat for dat in data]         

# print(data)

# ======================================================================================================================

# Q20. Implementing a Custom Sort Function

tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False}
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").

order_of_importance = {"High": 1, "Medium": 2, "Low": 3}
# sorted_on_priority = sorted(tasks, key = lambda priority: order_of_importance.get(priority["priority"], 0))
# sorted_on_completed = sorted(tasks, key = lambda completed: completed["completed"])
sorted_tasks = sorted(tasks, key = lambda task: (task["completed"], order_of_importance.get(task["priority"], 0))) # shakey

# print(sorted_tasks)
# person = {
#   "name": "Siya Kolisi",
#   "age": 32,
#   "country": "South Africa",
#   "sport": "Rugby"
# }

# # access
# print(person, type(person))
# print(person["name"])

# # update
# person["age"] += 1

# #methods
# #Iterable -> list, tuple, dict_keys
# print(person.keys()) #outputs the keys
# print(person.values()) #outputs the values
# print(person.items()) #outputs the key-value pairs as tuples

# loop
person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
  "address": {"city"},
  "sport": "Rugby"
}

# for details in person.items():
#   print(details[1])

# for key, value in person.items(): #with unpacking
#   print(key,value)

# # safely accessing items
# print(person.get("height")) # returns none if height is not a key.
# print(person.get("height", 186)) # returns 186 as a default if height is not found.

# #Nested dictionaries
# print(person["address"]["city"])
# #avoiding errors with nested missing data
# print(person.get("stats", {}).get("points", "No points data"))

# #creating a new dictionary with dictionary comprehension
# nums = {x: x**2 for x in range(10) if x % 2 == 0}}
# print(nums)
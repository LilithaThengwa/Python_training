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
# print(person.keys())
# print(person.values())
# print(person.items())

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

print(person["address"]["address"])
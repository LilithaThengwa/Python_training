classes = {
  "Class A": [
      {"name": "Alice", "grades": [82, 90, 88]},
      {"name": "Bob", "grades": [78, 81, 86]},
      {"name": "Charlie", "grades": [85, 85, 87]}
  ],
  "Class B": [
      {"name": "Dave", "grades": [92, 93, 88]},
      {"name": "Eve", "grades": [76, 88, 91]},
      {"name": "Frank", "grades": [88, 90, 92]}
  ]
}

#task 1

stud_ave = []

# for classs in classes.values(): #values returns values of dictionary as list
#   for stud in classs:
#     stud_ave.append(sum(stud["grades"]) / len(stud["grades"]))

# stud_ave = [sum(stud["grades"]) / len(stud["grades"]) for _class in classes.values() for stud in _class] #works

print(stud_ave)

#==================================================================

# Task 2 - Grades per student

# for classs in classes.values():
#   for stud in classs:
#     print(f"\n{stud['name']} grades: {stud['grades']} \nand average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.")

#==================================================================

# Grades per student, per class

for classs in classes.values():
  # print(f"\n{classs[0]['name']} grades: {classs[0]['grades']} \n")
  print(classs)
  # for stud in classs:
  #   print(f"\n{stud['name']} grades: {stud['grades']} \nand average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.")
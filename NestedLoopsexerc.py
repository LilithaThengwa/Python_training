from pprint import pprint

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

# stud_ave = []

# for classs in classes.values(): #values returns values of dictionary as list
#   for stud in classs:
#     stud_ave.append(sum(stud["grades"]) / len(stud["grades"]))

# # stud_ave = [sum(stud["grades"]) / len(stud["grades"]) for _class in classes.values() for stud in _class] #works

# print(stud_ave)

#================================================================

# Task 2 - Grades per student

# for classs in classes.values():
#   for stud in classs:
#     print(f"\n{stud['name']} grades: {stud['grades']}; average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.")

#================================================================

# Grades per student, per class

# for classs in classes.values():
#   print(f"\n{classs[0]} \n")
#   for stud in classs:
#     print(f"{stud['name']} grades: {stud['grades']}; average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.")

  # for stud in classs:
  #   print(f"\n{stud['name']} grades: {stud['grades']} \nand average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.")

#================================================================

# Actual task 1: Class average

# ave = []

# for classs, students in classes.items():
#   # print(type(classs))
#   # print(stud)
#   for stud in students:
#     ave.append(sum(stud["grades"]) / len(stud["grades"]))
#   pprint(f"{classs}: {sum(ave) / len(ave)/100:.2%}")

#better
# classave = {}
# for classs, students in classes.items():
#   for stud in students:
#     ave.append(sum(stud["grades"]) / len(stud["grades"]))

#   classave[classs] = sum(ave) / len(ave)

# print(classave)

#================================================================

# Actual task 2: Class average, per student

# #old
# for classs , students in classes.items():
#   print(f"\n{classs} \n")
#   stud_aves = {}
#   stud_aves["classname"] = classs 
#   for stud in students:
#     print(f"{stud['name']} average: {(sum(stud['grades']) / len(stud['grades']))/100:.2%}.\n")

# stud_aves = {}

# for classs , students in classes.items():
#   students_dict = {}
#   for stud in students:
#     students_dict[stud["name"]] = (sum(stud['grades']) / len(stud['grades']))
#   stud_aves[classs] = students_dict
# pprint(stud_aves)

#===============================================================

# Task 1 with comprehension

def find_avg(nums):

  return round(sum(nums) / len(nums), 2)


# classes_avg = {}

# for cls_name, students in classes.items():
#   class_students_avg = []
#   for student in students:
#     class_students_avg.append(find_avg(student['grades']))
#   classes_avg[cls_name] = find_avg(class_students_avg)
# print(classes_avg)

# students_avg_dict = {}
# for cls_name, students in classes.items():
#   students_avg_dict[cls_name] = {student['name']: find_avg(student['grades'])  for student in students}

# pprint(students_avg_dict)


#===============================================================

# Task 2 with comprehension

students_avg_dict = { cls_name: {student['name']: find_avg(student['grades'])
   for student in students}
  for cls_name, students in classes.items()
}

print(students_avg_dict)

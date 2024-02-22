# # Like lists but can only have unique values. Mutable, no duplicates. Sets have no guaranteed order, adding adds anywhere.

# # creation
# tec_gadgets = {"smartphon", "smartwatch", "laptop", "tablet"}
# tec_gadgets2 = {"smartphon", "smartwatch", "laptop", "tablet", "tablet"}# only has one tablet
# tec_lis= ["smartphon", "smartwatch", "laptop", "tablet", "tablet"]

# my_set = set()# for empty set

# #crud
# tec_gadgets.add("E-reader")
# more_gadgets = []


# colors = ["red", "blue", 'red', "green", "pink", "blue"]

# colors_set = set()
# for color in colors:
#   colors_set.add(color)
# set = set(colors)

# print(colors, colors_set)

#=========================================================

outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1
# Which are outdoor_gadgets ? 
# {'Smartwatch',  'Drone'}

typegadget = set()

for gadget in activity_gadgets:
  if activity_gadgets[gadget] in outdoor_activities:
    typegadget.add(gadget)

# print(typegadget)

#=========================================================

# Task 2
# # Which are indoor_gadgets ?

# typegadget = {gadget for gadget in activity_gadgets if activity_gadgets[gadget] in indoor_activities}

# print(typegadget)

#=========================================================

# Task 3/4

def outorindoor(gadgets, activities):
  return  {gadget for gadget in activity_gadgets if activity_gadgets[gadget] in activities}

print(outorindoor(activity_gadgets, outdoor_activities))

#=========================================================




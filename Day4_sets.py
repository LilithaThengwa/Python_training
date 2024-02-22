# Like lists but can only have unique values. Mutable, no duplicates. Sets have no guaranteed order, adding adds anywhere.

# creation
tec_gadgets = {"smartphon", "smartwatch", "laptop", "tablet"}
tec_gadgets2 = {"smartphon", "smartwatch", "laptop", "tablet", "tablet"}# only has one tablet
tec_lis= ["smartphon", "smartwatch", "laptop", "tablet", "tablet"]

my_set = set()# for empty set

#crud
tec_gadgets.add("E-reader")
more_gadgets = []


colors = ["red", "blue", 'red', "green", "pink", "blue"]

colors_set = set()
for color in colors:
  colors_set.add(color)
set = set(colors)

print(colors, colors_set)

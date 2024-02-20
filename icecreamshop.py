# #task 1
# stock1 = "vanilla"
# stock2 = "lime"
# stock3 = "chocolate"

# requested = input("Enter your ice cream flavour: ")

# if (requested == stock1 or requested == stock2 or requested == stock3):
#   print("Yes we have it")
# else:
#   print("Sorry we don't have it")

#task2
shop_stock = "vanilla, lime, chocolate"

requested = input("Which flavour: ")

# if (requested in shop_stock):
#   print("Yes we have it")
# else:
#  print("Sorry we don't have it")

y = "yes we have it" if requested in shop_stock else "Sorry we don't have it"

print(y)
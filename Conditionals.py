person1 = input("Enter your name: ")
height1 = float(input("Enter your height: "))
person2 = input("Enter your name: ")
height2 = float(input("Enter your height: "))

if (height1 > height2):
  print(f"{person1} is taller.")
elif (height1 == height2):
  print(f"{person1} and {person2} are the sameheight.")
else:
  print(f"{person2} is taller.")
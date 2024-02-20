# If is terminated with a colon(:). Indentation important.
# Elif instead of else. As many elifs as needed, one else.
# In is also called a memnership operator and returns a boolean.
# Refactoring is changing code to increase its quality while keeping dunctonality the same.
# Binary operators take two operands. >, <, >=, <=, ==, !=, in, and, or. Arithemtic and comparison operators.
# Unary operators take one operand. ~ is an example(has no practical use).
# Bitwise operators take two operands. &, |, ^, <<, >>, ~.
# Ternary operator is a short hand for if else. Take 3 operands. ___ if condition else ___.

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
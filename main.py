completed = input("Enter: ")
c = int(completed) 
d = "=" * int(c/10)
rem = 10 - c
print(f"[{d}]")

per = int(input("Please enter the percentage: "))

eq = per // 10

print(f"Output: [{('=' * eq) + ' ' * (10 - eq)}] {per}%")

# radius = float(input("Enter radius of circle: "))

# area = 3.14 * radius ** 2

# print(area)

r = input("Enter: ")
area = 3.14 * float(r) ** 2
print(area)

year = input("year of birth? ")

age = 2024 - int(year)

print(f"Your age is {age}")

temp= input("Enter temp: ")
temp = float(temp)
print((temp-32)*( 5/9))
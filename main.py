completed = input("Enter: ")
c = int(completed) 
d = "=" * int(c/10)
rem = 10 - c
print(f"[{d}]")

perc = int(input("enter the percentage: "))

x = perc // 10

print(f"Output: [{('=' * x) + ' ' * (10 - x)}] {perc}%")

r = input("Enter: ")
area = 3.14 * float(r) ** 2
print(area)

year = input("year of birth? ")

age = 2024 - int(year)

print(f"Your age is {age}")

temp= input("Enter temp: ")
temp = float(temp)
print((temp-32)*( 5/9))
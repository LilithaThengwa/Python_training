# # task1
# rows = input("Enter rows: ")
# i = 1
# while i <= int(rows):
#   print(("😒" + " ") * i)
#   i += 1

# rows = int(input("Enter rows "))
# for i in range(1, rows + 1):
#   print(("🤩" + " ") * (i))
#task2

#task3
# player_stats = [10, 30, 60]
# player_stats1 = player_stats.copy()

# for i in range(0, len(player_stats)):
#   player_stats1[i] = player_stats[i] * 2

# print(player_stats1)
# print(f"Power up: {power_up_stats} player stats: {player_stats}")

# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]

#task3

# filtered_names = []

# for avenger in avengers:
#   if len(avenger) > 10:
#     filtered_names.append(avenger)
# print(filtered_names)

# with list comprehension
# filtered_names = [avenger for avenger in avengers if len(avenger) > 10]

# print(filtered_names)

#21/02/24 exercises

# numbers = [8, 5, 7, 4, 6, 2]

# oddEven = ["Even" if i % 2 == 0 else "odd" for i  in numbers]

# print(oddEven)

# With for loop
numbers = [8, 5, 7, 4, 6, 2]
numbers_copy = []

for num in numbers:
  numbers_copy.append("Even" if num % 2 == 0 else "odd")

print(numbers_copy)


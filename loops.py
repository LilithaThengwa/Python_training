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

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

count = [len(avenger) for avenger in avengers ]
print(count)



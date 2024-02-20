# while i <= int(rows):
#   print(("😒" + " ") * i)
#   i += 1

#task2

#task3
# player_stats = [10, 30, 60]
# player_stats1 = player_stats.copy()

# for i in range(0, len(player_stats)):
#   player_stats1[i] = player_stats[i] * 2

# print(player_stats1)

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

# avcount = avengers.copy()

# for i in range(0, len(avengers)):
#   avcount[i] = str(avengers[i].count)

# print(avcount)

counts = [avenger.count(avenger) for avenger in avengers]
print(counts)



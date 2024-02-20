marks = [98, 75, 40, 80, 90, 45, 80, 60]
# marks.pop()
# print(marks)

# marks.pop(3) ##removes item at index

# print(marks[0:-3]) ## remove last three (same as print(marks[:-3])]).

# end_index = len(marks) - 3
# print(end_index)
# print(marks[0:end_index])
# print(marks)

# eng = 88
# marks.append(eng) #mutation
# print(marks)

# sci = 85
# marks.insert(2, sci)
# print(marks)

# price_list1 = [1000, 1500, 400]
# price_list2 = [2000, 5000]

# print(price_list1 + price_list2) #no mutation, new list.

# print([5 , 6] * 2) #[5, 6, 5, 6]

#copy
# price_list = [1000, 1500, 400]
# price_list_copy = price_list

# print(price_list.append(300))
# print(price_list_copy.append(200))

# print(price_list, price_list_copy)

#the above creates a shallow copy. Which means that the new list is a reference to the original list.

## deep copy (using slice)
# price_list = [1000, 1500, 400]
# price_list2 = price_list[:]

# print(price_list.append(300))
# print(price_list2.append(200))

# print(price_list, price_list2) #id to check memory indexs(id(price_list))

# price_list3 = price_list.copy()

# print(price_list3)

# subjects = ["maths", "physics", "chemistry", "biology"]
# print(", ", join(subjects))
# subjects.sort()
# subjects.sort(reversed = True)

#Task1

scrambledmsg = "world the save to time no is there"

scrambleList = scrambledmsg.split(" ")

# scrambleList.sort(reverse = True)
unscrambled = scrambleList[::-1]
print(scrambleList)


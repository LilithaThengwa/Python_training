#multiple variable assignment
# a, b, c = 1, 2, 3
# a = b = c = 10

# t1, t2, t3 = [100, 200, 300, 400]
# print(t1, t2, t3) #error

# t1, t2, t3, _ = [100, 200, 300, 400]
# print(t1, t2, t3) #works, _ => skip

# t1, t2, *t3 = [100, 200, 300, 400, 40, 60, 80]
# print(t1, t2, t3) # * upacking operator. t3 is list of 300, 400, 40, 60, 80 

#task
coordinate = [(5,4), (1,1), (6,20), (9, 10)]

import math

dist = []

for cord in coordinate:
  dist.append(math.sqrt((cord[0] **2) + (cord[1] **2))) 
print(dist) 

  

dist = [(math.sqrt((x ** 2) + (y ** 2))) for x, y in coordinate]

print(dist)




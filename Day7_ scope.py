# def add(x):
#     def add1(y):
#         x + y
#     return add1

# print(add(10)(5))

def fun(nums=[]):
    nums.append(10)
    print(nums)
   
fun() # [10]
fun() # [10, 10]
fun() # [10, 10, 10]
fun() # [10, 10, 10, 10]  
 
def fun(nums=[10]):
    if(nums == []):
      nums.append(10)
    print(nums)
 
# Expectation
fun() # [10]
fun() # [10]
fun() # [10]
fun() # [10]  
nums = [5, 10, 20]
nums_iter = iter(nums) # iter to create an iterator
# print(next(nums_iter)) # 5
# print(next(nums_iter)) # 10
# print(next(nums_iter)) # 20

# Iterators vs. Iterables
# Iterables can be looped multiple times and include methods like __iter__. Have potentially high memory usage. Has no knowledge of loop position. Eager evaluation strategy.
# Iterators can be looped over only once, supporting methods like __next__ and __iter__. Memory efficient. Know current position in loop. Lazy evaluation stretegy.

#Looping over an iterator

while True:
    try:
        print(next(nums_iter))
    except StopIteration:
        break

# Creating your own iterator
    
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
          raise StopIteration
        self.current += 1
        return self.current - 1
    
# Generators

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Generators simplify creating iterators. Use the yield keyword to pause function execution and save state.

# Infinite sequences with generators
        
def infinite_integers():
    n = 0
    while True:
        yield n
        n += 1


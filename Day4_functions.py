# a = 8
# b = 10

# print(a + b)

# def funcname(params):
#   return params

# #default values
# def driving(name, age=15, car="Tazz"):#default should be last
#   if age >= 18:
#     return f"{name} eligible, tested with {car}"
#   else:
#     return "Try again later"

#types of argument: Position and Keyword
# print(driving(name="Dhara", age=21))#keyword argument
#print(driving(20, "Gemma"))#order matters, position argument

#=========================================================

#lambda functions are anonymous, one line functions. Implicitly return(automatically). Useful for passing functions as arguments.

# add = lambda a, b: a + b

# def say_hello():
#   return "hello, "

# def greeting(hello_message, name):
#   print(hello_message() + name)

# greeting(say_hello, "Caleb")

# def map_own(fn, arr):   
#   return [fn(val) for val in arr]

# print(map_own(lambda x: x * 2, [1, 2, 3]))

# def sayHello():
#  def msg():
#   return 'Hello, 🎊'
#  return msg

# print(sayHello()())

# mul = lambda x: lambda y: x * y

# print(mul(3)(6))

print(any(True, False, True))

print(any([True, False, True]))
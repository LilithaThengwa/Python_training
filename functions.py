a = 8
b = 10

print(a + b)

def funcname(params):
  return params

#default values
def driving(name, age, car="Tazz"):#default should be last
  if age >= 18:
    return f"{name} eligible, tested with {car}"
  else:
    return "Try again later"

#types of argument: Position and Keyword
print(driving(17, "BMW"))
print(driving(21, "Dhara"))#error
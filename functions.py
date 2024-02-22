a = 8
b = 10

print(a + b)

def funcname(params):
  return params

#default values
def driving(name, age=15, car="Tazz"):#default should be last
  if age >= 18:
    return f"{name} eligible, tested with {car}"
  else:
    return "Try again later"

#types of argument: Position and Keyword
print(driving(name="Dhara", age=21))#keyword argument
#print(driving(20, "Gemma"))#order matters, position argument
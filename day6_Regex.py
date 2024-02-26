import re

names = ["  John Doe  ", "  Jane   Smith", "Alice Johnson  ", "ChrisEvans"]

# result = re.sub(r"(\w+) (\w+)", r"\2, \1", str(names))

# print(type(result))

# res2 = []
# for name in names:
#   res2.append(re.sub(r"\s*(\w+)\s+(\w+)\s*", r"\2, \1", name))

# print(res2)

output = [re.sub(r'\s*(\w+)\s+(\w+)\s*',r'\2, \1', name) for name in names]
print(output)
#Strings are immutable, the original string doesn't change.
# .upper(), .lower(), .title(), .capitalize().
# .find() returns the index(interger) and returns -1 if not found.
#strip() removes whitespace from the beginning and end of the string.
#strip("") removes the specified character.
# rstript() removes the specified character from the end. #lstrip() removes the specified character from the beginning,
# .strip().rstip().upper() is dot chaining.

# #task1
# message = "    🚨🔍📱🔑secret_code✌️"
# code = "SECRET_CODE✌️"

# keyIndex = message.find("🔑")
# output = message[keyIndex + 1:].upper()

# if (output == code):
#   print("correct.")
# else:
#   print("incorrect.")

#task2

# message = "    🚨🔍📱secret_code✌️"
# code = "SECRET_CODE✌️"

# if ("🔑" not in message):
#   print("no key")
  
# else:
#   keyIndex = message.find("🔑")
#   output = message[keyIndex + 1:].upper() 
#   if (output.upper() == code):
#     print("correct.")
#   else:
#     print("incorrect.")

    
#task3

message = "    🚨🔍📱🔑****secret_code✌️((((("
code = "SECRET_CODE✌️"

if ("🔑" not in message):
  print("no key")

else:
  keyIndex = message.find("🔑")
  output = message[keyIndex + 1:].upper().strip(" (").strip("*").strip(")")
  if (output.upper() == code):
    print("correct.")
  else:
    print("incorrect.")


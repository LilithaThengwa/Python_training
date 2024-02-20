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


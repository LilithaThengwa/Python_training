roomsList = [
  {"room_number": 0, "bed_type": "king", "smoking": False, "availability": True}, 
  {"room_number": 1, "bed_type": "queen", "smoking": False, "availability": True}, 
  {"room_number": 2, "bed_type": "double", "smoking": True, "availability": True},
  {"room_number": 3, "bed_type": "single", "smoking": False, "availability": False},
  {"room_number": 4, "bed_type": "king", "smoking": False,
"availability": True}]

def add_room(rooms, room_number, bed_type, smoking):
  
  room = {"room_number": room_number, "bed_type": bed_type, "smoking": smoking, "availability": "True"}#new rooms always availa")
  
  roomsList.append(room)
  return roomsList

print(add_room(5, "king", False))

# def book_room(preferred_bed_type = "Double", smoking_preference = False):
#   for room in roomsList:
#     if (preferred_bed_type == room["bed_type"] and smoking_preference == room["smoking"] and room["availability"] == "True"):
#       room["availability"] = "False"
#       return f"Room number {room['room_number']} is booked successfuly."

# # print(book_room("king", False))

# def list_available_rooms(rooms):
#   return [room for room in rooms if room["availability"] == True]

# print(list_available_rooms(roomsList))
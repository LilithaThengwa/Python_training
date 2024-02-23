roomsList = [
  {"room_number": 0, "bed_type": "king", "smoking": False, "availability": True}, 
  {"room_number": 1, "bed_type": "queen", "smoking": False, "availability": True}, 
  {"room_number": 2, "bed_type": "double", "smoking": True, "availability": True},
  {"room_number": 3, "bed_type": "single", "smoking": False, "availability": False},
  {"room_number": 4, "bed_type": "king", "smoking": False, "availability": True}]

#=================================================================

#Add a room

def add_room(rooms, room_number = 10, bed_type = "double", smoking = False):  
  newroom = {"room_number": room_number, "bed_type": bed_type, 
  "smoking": smoking, "availability": "True"} #new rooms always available")  
  rooms.append(newroom)
  return rooms

# print(add_room(roomsList, 5, "king", False))

#===============================================================

# Book a room

def book_room(rooms, preferred_bed_type = "double", smoking_preference = False):
  for room in rooms:
    if (preferred_bed_type == room["bed_type"] and 
      smoking_preference == room["smoking"] and 
      room["availability"] == True):
      room["availability"] = False
      return f"Room number {room['room_number']} is booked successfuly."

  else:
    return "No rooms matching preferrence available"

# print(book_room(roomsList, "king", False))
# print(book_room(roomsList)) #using default values

#===============================================================

# List all available rooms

def list_available_rooms(rooms):
  return [room for room in rooms if room["availability"] == True]

# print(list_available_rooms(roomsList))
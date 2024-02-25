# Exercise: Event Registration System
# Objective: Write a Python program that includes a function to register participants for an event. The registration function should handle participant details and their preferences with default values for some parameters.
# Initial Setup
# Participants need to provide their name and email. Additionally, they can specify their meal preference (vegetarian or non-vegetarian) and if they need accommodation. By default, the meal preference should be set to "non-vegetarian", and accommodation required should be False.
# Task
# Registration Function: Write a function register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False) that registers a participant with their provided details and preferences.
# Display Registered Participants: After registration, display the participant's details, including their name, email, meal preference, and accommodation needs.
# Expected Functionality
# Registering a participant with all details specified.
# Registering a participant with only the name and email, using default values for the other parameters.

participants = []

def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation = False):
  new_participant = {"name": name, "email": email, "meal_preference": meal_preference, "needs_accommodation": needs_accommodation}
  participants.append(new_participant)


def display_registered_participants(registered_participants):
  for participant in participants:
    print(f"Name: {participant['name']} \nEmail: {participant['email']} \nMeal Preference: {participant['meal_preference']} \nAccommodation: {participant['needs_accommodation']}")



register_participant("JJ", "qpmzj@example.com", "vegetarian", True)
display_registered_participants(participants)

from datetime import datetime

# def calculate_age():
#     age = int(input("Year of birth: "))
#     re  = datetime.now().year - age
#     return re

# def calculate_age(): #handling runtime errors
#     # age = int(input("Year of birth: "))w
#     try:
#         age = int(input("Year of birth: "))
#         print(f"Age: {datetime.now().year - age}")
#     except ValueError as e:  
#         print("Invalid value type: ", e)
#     else:
#         print("Success")
#     finally:
#         print("Done")

def calculate_age(): #handling logical errors
    try:
        age = int(input("Year of birth: "))
        if(age < 0):
            raise ValueError("Year cannot be negative")
        elif (age > datetime.now().year - age):
            raise ValueError("You are not from the future.")
        print(f"Age: {datetime.now().year - age}")
    except ValueError as e:  
        print("Invalid value type: ", e)
    except Exception as e: #catch all for errors
        print("You really messed up.", e)

#================================================================================================================================
        
#Create your own error class
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers not allowed."
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} --> {self.message}"
    
def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)#instance of NegativeNumberError created here
        
    #just match, not creating instance
    except NegativeNumberError as e:
        print(e)

if __name__ == "__main__":
#    print(calculate_age())
    only_positive_num()
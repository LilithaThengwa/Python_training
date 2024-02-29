# @property
- A built-in decorator in Python. 
- Helpful when defining properties with minimal effortwithout manually calling the property() function.
- Simplifies the usage of getters and setters.

## example

class Bank:

    def __init__(self, acc):
        self.acc = acc

    @property
    def name(self): # getter method
        return self._acc

    @name.setter
    def name(self, acc): # setter method
        self._acc = acc

# Setter
- A method that makes it possbible to define a setter method for an attribute in a class.
- Modifies the value in a controlled way.

## example
- Included above.
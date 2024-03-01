class Circle:
    pi = 3.14159

    def __init__(self, radius):
       self.radius = radius

    def calculate_area(self):
        return self.pi * (self.radius**2)
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
        
    @staticmethod
    def perimeter(radius):
        return 2 * Circle.pi * radius

circle1 = Circle(2)

print(circle1.calculate_area())

print(circle1.perimeter(10))

circlefromdia = Circle.from_diameter(10) 
print(circlefromdia.calculate_area())

# Ecapsulation: Achieved through the use of private variable and methods.
# Inheritance: Allows for code ruse and extension across classes.
# Polymorphism: Enables objects to implement the same methods in different ways.
# Static and Class Methods: Provide utility functions that are relevant to the class rather than any instance.
# Magic Methods: Enhance the functionality of our objects, making them more Pythonic and intuitive to use.

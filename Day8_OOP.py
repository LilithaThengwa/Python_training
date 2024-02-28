class Circle:
    pi = 3.14

    def __init__(self, radius):
       self.radius = radius

    def calculate_area(self):
        return self.pi * (self.radius**2)
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)
        
    @staticmethod
    def perimeter(rad):
        return 2 * Circle.pi * rad

circle1 = Circle(2)

print(circle1.calculate_area())

print(circle1.perimeter(10))

circlefromdia = Circle.from_diameter(10) 
print(circlefromdia.calculate_area())
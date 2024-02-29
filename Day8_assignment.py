# class Bank:

#     def __init__(self, acc):
#         self.acc = acc

#     @property
#     def name(self): # getter method
#         return self._acc

#     @name.setter
#     def name(self, acc): # setter method
#         self._acc = acc

from functools import wraps

def Adecorator(func):

    @wraps(func)
    def wrapper(name):
        func(name.upper())
    return wrapper

@Adecorator
def What(name):
    print(name)

print(What("joe"))

#A decorator for turning strings to uppercase when printing.

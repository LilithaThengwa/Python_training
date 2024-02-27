# Car --> blueprint | Class blueprint object
#DRY
class Car:
    def __init__(self, name, engine, wheels, doors):
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors

# self --> to the object created
# ferrari --> object

ferrari = Car("Ferrari", "V8", 4, 2)
toyota = Car("Toyota", "V4", 4, 4)
porsche = Car("911", "V6", 4, 2)

# print(ferrari.name, ferrari.wheels)
# print(toyota.name, toyota.wheels)

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return (f"Your balance is: R{self.balance:,}")

    def withdraw(self, amount):
        if(self.balance >= amount):
          self.balance = self.balance - amount
          return (f"Succes. Your balance is: R{self.balance:,}")
        else:
            return (f"Failed. Your balance is: R{self.balance:,}")
        # self.balance = self.balance - amount if self.balance >= amount else "broke"

    def deposit(self, amount):
        self.balance = self.balance + amount
        return (f"Succes. Your balance is: R{self.balance:,}")
    
gemma = Bank(123, "Gemma", 15_000)

gemma.withdraw(12000)

print(gemma.display_balance())

gemma.deposit(5000)

print(gemma.display_balance())


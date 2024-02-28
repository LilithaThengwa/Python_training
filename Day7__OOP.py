# # Car --> blueprint | Class blueprint object
# #DRY
# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

# # self --> to the object created
# # ferrari --> object

# ferrari = Car("Ferrari", "V8", 4, 2)
# toyota = Car("Toyota", "V4", 4, 4)
# porsche = Car("911", "V6", 4, 2)

# # print(ferrari.name, ferrari.wheels)
# # print(toyota.name, toyota.wheels)

class Bank:
    interest = 0.2
    totalacc = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
        Bank.totalacc += 1

    @classmethod
    def update_interest_rate(cls, rate):
        Bank.interest = rate

    # @classmethod
    # def get_totalaccounts(cls):
    #     return cls.totalacc
    
    @staticmethod #better
    def get_totalaccounts(cls):
        return cls.totalacc
        
    def display_balance(self):
        return (f"Your balance is: R{self.__balance:,}")

    def withdraw(self, amount):
       if(self.__balance >= amount):
          self.__balance -= (amount)
          return (f"Succes. {self.display_balance()}")
       else:
            return (f"Failed. {self.display_balance()}")
        # self.balance = self.balance - amount if self.balance >= amount else "broke"

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return (f"Succes. Your balance is: R{self.__balance:,}")
    
    def apply_interest(self):
       self.__balance += self.__balance * self.interest

    def getbalance(self):
        return self.__balance
     
# gemma = Bank(123, "Gemma", 15_000)
# alex = Bank(456, "Alex", 15_000)

# # gemma.withdraw(12000)
# gemma.apply_interest()
# print(gemma.display_balance())

# gemma.deposit(5000)

# print(gemma.display_balance())

# print(Bank.get_totalaccounts())

# class SavingsAccount(Bank):
#     interest = 0.1

    # def __init__(self, acc_no, name, balance):
    #     super().__init__(acc_no, name, balance)
    #     self.__balance = balance

    # # def display_balance(self):
    # #     return (f"Your balance is: R{self.__balance:,}")

    # # def apply_interest(self):
    # #    self.__balance += self.__balance * SavingsAccount.interest

# class CheckingAccount(Bank):
#     def __init__(self, acc_no, name, balance):
#         super().__init__(acc_no, name, balance)
#         self.__balance = balance

#     def display_balance(self):
#         return (f"Your balance is: R{self.__balance:,}")
        
#     def withdraw(self, amount):
#        if(self.__balance >= amount + 1):
#           self.__balance -= (amount + 1)
#           return (f"Succes. {self.display_balance()}")
#        else:
#             return (f"Failed. {self.display_balance()}")
       
class CheckingAccount(Bank):

    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance)

    def display_balance(self):
        return (f"Your balance is: R{self.getbalance:,}")
    
    def withdraw(self, amount):
       withfee = amount + 1
       super().withdraw(withfee)

# gemma = SavingsAccount(123, "Gemma", 15_000)
alex = CheckingAccount(126, "Alex", 10_000)
# gemma.apply_interest()
# print(gemma.display_balance())
alex.withdraw(3_000)
print(alex.display_balance())


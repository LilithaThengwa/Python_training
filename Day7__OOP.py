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


#==================================================================================================================================

class Bank:
    interest_rate = 0.02
    totalacc = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance #private variable
        Bank.totalacc += 1

    @classmethod
    def update_interest_rate(cls, rate):
        cls.interest_rate = rate

    # @classmethod
    # def get_totalaccounts(cls):
    #     return cls.totalacc
    
    @staticmethod #better
    def get_totalaccounts(cls):
        return f"In total we have {cls.totalacc} accounts"
        
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
       self.__balance += self.__balance * self.interest_rate

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

#==========================================================
    
class SavingsAccount(Bank):
    interest_rate = 0.05

    def apply_interest(self):
       super().apply_interest()
class CheckingAccount(Bank):
    transaction_fee = 1
    
    def withdraw(self, amount):
       withfee = amount + CheckingAccount.transaction_fee
       super().withdraw(withfee)

    def __str__(self):
        return f"Account {self.acc_no} owned by {self.name} with balance: R{self.getbalance():,}"

    def __repr__(self):
        return f"CheckingAccount ('{self.acc_no}','{self.name}', '{self.getbalance():,}'"

    def __add__(self, other):
        return self.getbalance() + other.getbalance()
    
gemma = SavingsAccount(123, "Gemma", 15_000)
alex = CheckingAccount(126, "Alex", 10_000)
gemma.apply_interest()
print(gemma.display_balance())
alex.withdraw(3_000)
print(alex.display_balance())
print(alex.__str__())


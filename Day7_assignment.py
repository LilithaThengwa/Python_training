from datetime import datetime
# class Invoice:
#     list_transactions = []
#     # transaction = {}
#     transaction_count = 0
#     def __init__(self, id, date, type, amount, transaction, listtransactions):
#         self.id = id
#         self.date = date
#         self.type = type
#         self.amount = amount
#         self.transaction = transaction
#         self.listtransactions = listtransactions

#     def add_transaction(self):


#     def list_transactions(self):
#         self.transaction = {}
#         self.transaction["id"] = self.id
#         self.transaction["date"] = self.date
#         self.transaction["type"] = self.type
#         self.transaction["amount"] = self.amount
#         self.listtransactions.append(self.transaction)  
#         # for key, value in self.listtransactions:
#         #     print(key)

#         return self.listtransactions


# inv = [{"id": 1, "date": 12, "type": "deposit", "amount": 3_000}]
# invoice = Invoice(1, 12, "withdraw", 2_000, {}, inv)
# print(invoice.list_transactions())

class Bank:
    interest = 0.2
    transaction_count = 0
    transaction_list = []

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
    
    @staticmethod #better
    def get_totalaccounts(cls):
        return cls.totalacc
        
    def display_balance(self):
        return (f"Your balance is: R{self.__balance:,}")

    def withdraw(self, amount):
       if(self.__balance >= amount):
          self.__balance -= (amount)
          self.transaction_count += 1
          self.transaction_list.append({"id": self.transaction_count, "date": datetime.now(), "type": "deposit", "amount": amount})
          return (f"Succes. {self.display_balance()}")
       else:
            return (f"Failed. {self.display_balance()}")

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.transaction_list.append({"id": self.transaction_count, "date": datetime.now(), "type": "deposit", "amount": amount})
        return (f"Succes. Your balance is: R{self.__balance:,}")
    
    def apply_interest(self):
       self.__balance += self.__balance * self.interest

    # def add_transaction(self):
    #    self.transaction_list.append(self, self.transaction_count, datetime.now(), "withdraw")
    
    def print_transactions(self):
        return print(self.transaction_list)

gemma = Bank(123, "Gemma", 15_000)
alex = Bank(456, "Alex", 15_000)

gemma.withdraw(12000)
gemma.apply_interest()
print(gemma.display_balance())
gemma.print_transactions()

# gemma.deposit(5000)

# print(gemma.display_balance())

# print(Bank.get_totalaccounts())

class Invoice:
    def __init__(self, id, date, type, amount, transaction, listtransactions):
        self.id = id
        self.date = date
        self.type = type
        self.amount = amount
        self.transaction = transaction
        self.listtransactions = listtransactions

    def list_transactions(self):
        self.transaction = {}
        self.transaction["id"] = self.id
        self.transaction["date"] = self.date
        self.transaction["type"] = self.type
        self.transaction["amount"] = self.amount
        self.listtransactions.append(self.transaction)  

        return self.listtransactions


inv = [{"id": 1, "date": 12, "type": "deposit", "amount": 3_000}]
invoice = Invoice(1, 12, "withdraw", 2_000, {}, inv)
print(invoice.list_transactions())

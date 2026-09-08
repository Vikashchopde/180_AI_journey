

class Payment:
    def pay(self, amount):
        print(f"paying {amount} using Payment method")

class UPI(Payment):
    def pay(self, amount):
        print(f"paying {amount} using UPI method")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"paying {amount} using Credit Card method")

class Cash(Payment):
    def pay(self, amount):
        print(f"paying {amount} using Cash method")

payments = [UPI(), CreditCard(), Cash()]

for payment in payments:
        payment.pay(1000)

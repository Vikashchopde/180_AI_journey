
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass 

# class UPI(Payment):
#     def pay(self, amount):
#         print(f"paying {amount} using UPI")

# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"paying {amount} using Credit Card ")


# upi = UPI()
# card = CreditCard()

# upi.pay(110000)
# card.pay(150000)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"paid {amount} using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"paid {amount} using Credit Card")

class Cash(Payment):
    def pay(self, amount):
        print(f"paid {amount} using Cash")

payments = [UPI(), CreditCard(), Cash()]

for payment in payments:
    payment.pay(100000)
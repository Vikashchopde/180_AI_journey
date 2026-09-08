
class BankAmount:
    def __init__(self, owner , balance , pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin 

    def show_balance(self, pin):
        if pin == self.__pin:
            return self._balance
        else :
            return "Invalid Pin"

    def deposit(self, amount , pin):
        if pin == self.__pin:
            self._balance += amount
            return f"Amount deposited successfully. New balance is {self._balance}"
        else:
            return "Invalid Pin"

    def withdraw(self, amount , pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount    
                return f"Amount withdrawn successfully. New balance is {self._balance}"
            else:
                return "Insufficient balance"
        else:
            return "Invalid Pin"


        
Balance = BankAmount("vikas", 100000 , 160920)
# print(Balance.show_balance(160921))
print(Balance.show_balance(160920))
print(Balance.deposit(10000 , 160920))
print(Balance.withdraw(5000 , 160920))

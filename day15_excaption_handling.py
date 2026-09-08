
# class InsufficientBalanceError(Exception):
#     pass

# try:
#     balance = 1000
#     withdraw_amount = float(input("Enter the amount to withdraw:"))
#     if withdraw_amount > balance:
         
#          raise InsufficientBalanceError("insufficient funds in your account.")
    
# except InsufficientBalanceError as e:
#     print(f"Error: {e}")

# else:
#     balance -= withdraw_amount
#     print(f"Withdrawal successful. Remaining balance: {balance}")

# finally:
#     print("Execution completed.")
            


class EmptyUsernameError(Exception):
    pass

class UnderAgeError(Exception):
    pass


try:
    username = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if username == "":
        raise EmptyUsernameError("username can't be empty")
    
    if age < 18:
        raise UnderAgeError("age must be greater then 18")

except EmptyUsernameError as e:
    print(f"Error: {e}")

except UnderAgeError as e:
    print(f"Error: {e}")

else: 
    print(f"registerd succesfull {username}")

finally:
    print("proccess completed")
     

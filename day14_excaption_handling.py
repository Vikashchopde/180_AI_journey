
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2 
#     print(result)
# except ValueError:
#     print("Invalid input! Please enter valid integers.")
# except ZeroDivisionError :
#     print("Error: Division by zero is not allowed.")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(result)

except ValueError:
    print("Invalid input! Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division performed successfully.")

finally:
    print("Execution completed.")

    


try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
 print(f"Invalid input: {e}")

else:
    print(f"Your age is: {age}")

finally:
    print("Execution completed.")

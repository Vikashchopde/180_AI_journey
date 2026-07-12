
name= input("What is your name? ")
age= int(input("What is your age ? "))
city= input("What is your city ? ")

def get_status(age):
    if (age) < 0:
        return "Invalid age"
    elif (age) <= 11:
        return "child"
    elif (age) <= 17:
        return "teenager"
    elif (age) <= 59:
        return "Adult"
    else:
       return "Senior citizen"

status = get_status(age);


print("\n========= Student Information System =========")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"City    : {city}")
print(f"Status  : {status}")



           
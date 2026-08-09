
def add(*numbers):
    total = 0
    for nums in numbers:
        total += nums 
    return total 


print(add(10, 20, 30))
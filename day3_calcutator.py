
choice = int(input(" choice between (1,5) : " ))
a = int(input("Enter First Number : " ))
b = int(input ("Enter Second Number : " ))

def smart_calculator(a , b , choice):
  if choice == 1:
   return a + b
  elif choice == 2:
   return a - b 
  elif choice == 3:
   return a * b
  elif choice == 4:
   return a / b
  else : 
   return "Invalid "
  
ans = smart_calculator(a,b,choice)
print(f"Result : {ans}")

 
   
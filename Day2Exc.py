# Excercise 1

def calculate(int1: int, int2: int):

    print(int1 + int2)
    print(int1 - int2)
    print(int1 * int2)

calculate(3,9)

# Excercise 4

n = int(input("Please enter the number to be checked.  "))

for number in range(2,n):
    if n % number == 0:
        print(str(n) + " is not a prime number")
        break

else:
    print(str(n) + " is a prime number")




import math_utils

a = 10
b = 5

print(f"Addition: {math_utils.add(a, b)}")        
print(f"Subtraction: {math_utils.subtract(a, b)}")  
print(f"Multiplication: {math_utils.multiply(a, b)}")  
print(f"Division: {math_utils.divide(a, b)}")      
     
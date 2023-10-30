import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
def sin(x):
     return math.sin(x)
def cos(x):
     return math.cos(x)
def tan(x):
    return math.tan(x)
def numsquare(x):
    return x*x
def inverse (x):
    return 1/x
def log(x):
    return math.log(x)

print("Select operation:")
print("1.Basic Arihtematics:")
print("2.other:")
choice=input("enter choice(1/2): ")
if choice=='1':
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice ==input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("enter the second number: ")) 
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")  
elif choice =='2':
    print("1. sin")
    print("2. cos")
    print("3. tan")
    print("4. numsquare ")
    print("5. inverse")
    print("6. log")
    choice = input("Enter choice (1/2/3/4/5/6): ")
    num1 = float(input("Enter  number: "))
    if choice =='1':
        print("The value of sin(",num1,") is : ",sin(num1))
        print("The value of sin(",-num1,") is: ",sin(-num1))
    elif choice =='2':
        print("the value of cos(",num1,")is:",cos(num1))
        print("the value of cos(",-num1,"):",cos(-num1))
    elif choice =='3':
        print("the value of tan(",num1,") is:",tan(num1))
        print("the value of tan(",-num1,")is:",tan(-num1))
    elif choice =='4':
        print("the square of the number(",num1,") is:",numsquare(num1))
    elif choice =='5':
        print("the inverse of number(",num1,") is:",inverse(num1))
    elif choice=='6':
        print("the logarithamic value of(",num1,") is:",log(num1))
    else:
        print("Invalid input")
else:
        print("Invalid input")

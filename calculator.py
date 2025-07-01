def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation: +, -, *, /")
choice = input("Enter choice: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '+':
    print(add(a, b))
elif choice == '-':
    print(subtract(a, b))
elif choice == '*':
    print(multiply(a, b))
elif choice == '/':
    print(divide(a, b))
else:
    print("Invalid input")

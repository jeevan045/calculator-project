history = []
def calculate_percentage(total, percentage):
    return (total * percentage) / 100


while True:
    print("\nSimple Calculator")
    print("Options: add, subtract, multiply, divide, history,percentage, exit")
    choice = input("Enter choice: ")

    if choice == "exit":
        break

    if choice == "history":
        print("Calculation History:")
        for item in history:
            print(item)
        continue
    if choice == "percentage":
        a = float(input("Enter the total"))
        b = float(input("ENter the number to calculate percentage"))
        print(calculate_percentage(a,b))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "add":
        result = num1 + num2
    elif choice == "subtract":
        result = num1 - num2
    elif choice == "multiply":
        result = num1 * num2
    elif choice == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            continue
    else:
        print("Invalid input")
        continue

    print("Result:", result)
    history.append(f"{num1} {choice} {num2} = {result}")

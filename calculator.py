history = []

while True:
    print("\nSimple Calculator")
    print("Options: add, subtract, multiply, divide, history, exit")
    choice = input("Enter choice: ")

    if choice == "exit":
        break

    if choice == "history":
        print("Calculation History:")
        for item in history:
            print(item)
        continue

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

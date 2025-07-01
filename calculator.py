history = []

# Function to calculate percentage
def calculate_percentage(total, percentage):
    return (total * percentage) / 100

# Function for Simple Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Function for Compound Interest
def compound_interest(principal, rate, time):
    return (principal * ((1 + (rate / 100)) ** time)) - principal


# Main calculator loop
while True:
    print("\n============================")
    print("   Welcome to Calculator App")
    print("============================")
    print("Options:")
    print("  add, subtract, multiply, divide")
    print("  percentage, interest, history, exit")

    choice = input("\nEnter your choice: ").lower()

    if choice == "exit":
        print("Exiting Calculator. Goodbye!")
        break

    # Show history
    if choice == "history":
        print("\nCalculation History:")
        if not history:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    # Percentage calculation
    if choice == "percentage":
        total = float(input("Enter the total value: "))
        percent = float(input("Enter the percentage to calculate: "))
        result = calculate_percentage(total, percent)
        print(f"\n✅ {percent}% of {total} is {result}")
        history.append(f"{percent}% of {total} = {result}")
        continue

    # Interest calculation
    if choice == "interest":
        print("\n📈 Interest Calculator")
        print("1. Simple Interest")
        print("2. Compound Interest")
        int_opt = input("Choose option (1 or 2): ")

        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time (in years): "))

        if int_opt == '1':
            result = simple_interest(principal, rate, time)
            print(f"✅ Simple Interest = {result}")
            history.append(f"Simple Interest of {principal} at {rate}% for {time} years = {result}")
        elif int_opt == '2':
            result = compound_interest(principal, rate, time)
            print(f"✅ Compound Interest = {result}")
            history.append(f"Compound Interest of {principal} at {rate}% for {time} years = {result}")
        else:
            print("⚠️ Invalid option for interest calculation.")
        continue

    # Basic arithmetic operations
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
        continue


    if choice == "add":
        result = num1 + num2
        symbol = '+'
    elif choice == "subtract":
        result = num1 - num2
        symbol = '-'
    elif choice == "multiply":
        result = num1 * num2
        symbol = '*'
    elif choice == "divide":
        if num2 != 0:
            result = num1 / num2
            symbol = '/'
        else:
            print("⚠️ Cannot divide by zero.")
            continue
    else:
        print("⚠️ Invalid input. Please choose a valid option.")
        continue

    print(f"\n✅ Result: {num1} {symbol} {num2} = {result}")
    history.append(f"{num1} {symbol} {num2} = {result}")

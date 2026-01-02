# app/cli.py
def run():
    """Runs the legitimate CLI calculator."""
    print("Welcome to Simple Calculator!")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operator"
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        if input("Continue? (y/n): ").lower() != 'y':
            break
    print("Calculator exiting.")
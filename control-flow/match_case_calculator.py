# match_case_calculator.py

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Match case to perform calculation
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation selected.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

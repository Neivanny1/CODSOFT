#!/usr/bin/python3

'''
Simple Calculator
'''

def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")
        
        # Get user inputs
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            # Perform calculation based on chosen operation
            if operation == '+':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Invalid operation selected. Please choose one of +, -, *, or /.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        # Ask the user if they want to perform another operation or quit
        choice = input("\nWould you like to perform another operation? (yes to continue, any other key to quit): ")
        if choice.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
if __name__ == '__main__':
    calculator()

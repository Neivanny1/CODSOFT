#!/usr/bin/python3

'''
Simple Calculator with ASCII Banner and Colors
'''

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII banner
def print_banner():
    print(Colors.BLUE + Colors.BOLD)
    print(r"""
     _______  __   __  _______  _______  _______  ______    _______ 
    |       ||  | |  ||       ||       ||       ||    _ |  |       |
    |    ___||  |_|  ||    ___||   _   ||   _   ||   | ||  |    ___|
    |   |___ |       ||   |___ |  | |  ||  | |  ||   |_||_ |   |___ 
    |    ___||       ||    ___||  |_|  ||  |_|  ||    __  ||    ___|
    |   |___ |   _   ||   |___ |       ||       ||   |  | ||   |___ 
    |_______||__| |__||_______||_______||_______||___|  |_||_______|
    """)
    print(Colors.ENDC)

# Calculator function
def calculator():
    print_banner()
    print(Colors.GREEN + "Welcome to the Simple Calculator!" + Colors.ENDC)
    
    while True:
        print("\nChoose an operation:")
        print(Colors.YELLOW + "1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)" + Colors.ENDC)
        
        # Get user inputs
        try:
            num1 = float(input(Colors.BOLD + "\nEnter the first number: " + Colors.ENDC))
            num2 = float(input(Colors.BOLD + "Enter the second number: " + Colors.ENDC))
            operation = input(Colors.BLUE + "Enter the operation (+, -, *, /): " + Colors.ENDC)

            # Perform calculation based on chosen operation
            if operation == '+':
                result = num1 + num2
                print(Colors.GREEN + f"The result of {num1} + {num2} is: {result}" + Colors.ENDC)
            elif operation == '-':
                result = num1 - num2
                print(Colors.GREEN + f"The result of {num1} - {num2} is: {result}" + Colors.ENDC)
            elif operation == '*':
                result = num1 * num2
                print(Colors.GREEN + f"The result of {num1} * {num2} is: {result}" + Colors.ENDC)
            elif operation == '/':
                if num2 == 0:
                    print(Colors.RED + "Error: Division by zero is not allowed." + Colors.ENDC)
                else:
                    result = num1 / num2
                    print(Colors.GREEN + f"The result of {num1} / {num2} is: {result}" + Colors.ENDC)
            else:
                print(Colors.RED + "Invalid operation selected. Please choose one of +, -, *, or /." + Colors.ENDC)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter numeric values." + Colors.ENDC)
        
        # Ask the user if they want to perform another operation or quit
        choice = input(Colors.BOLD + Colors.YELLOW + "\nWould you like to perform another operation? (yes to continue, any other key to quit): " + Colors.ENDC)
        if choice.lower() != 'yes':
            print(Colors.BLUE + "Thank you for using the calculator. Goodbye!" + Colors.ENDC)
            break

# Run the calculator
if __name__ == '__main__':
    calculator()

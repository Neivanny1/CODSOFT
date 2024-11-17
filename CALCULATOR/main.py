#!/usr/bin/python3

'''
Simple Calculator with ASCII Banner and Colors
'''

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[38;5;214m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII banner
def print_banner():
    print(Colors.BLUE + Colors.BOLD)
    print(r"""
       ____      _            _        _             
  / ___|__ _| | ___ _   _| | __ _ | |_ ___   ___ 
 | |   / _` | |/ __| | | | |/ _` || __/ _ \ / _ \
 | |__| (_| | | (__| |_| | | (_| || || (_) |  __/
  \____\__,_|_|\___|\__,_|_|\__,_| \__\___/ \___|

    """)
    print(Colors.ENDC)

# Calculator function
def calculator():
    print_banner()
    print(Colors.GREEN + "Welcome to the Scientific Calculator!" + Colors.ENDC)
    
    while True:
        print(Colors.ORANGE + "\nOperations Supported:\n===================== \n" + Colors.ENDC)
        print(Colors.YELLOW + "1: Addition (+)")
        print("2: Subtraction (-)")
        print("3: Multiplication (*)")
        print("4: Division (/)")
        print("5: Modulus (%)")
        print("6: Exponentiation (**)")
        print("7: Bitwise AND (&)")
        print("8: Bitwise OR (|)")
        print("9: Bitwise XOR (^)" + Colors.ENDC)
        
        # Get user inputs
        try:
            num1 = float(input(Colors.BOLD + "\nEnter the first number: " + Colors.ENDC))
            num2 = float(input(Colors.BOLD + "Enter the second number: " + Colors.ENDC))
            operation = input(Colors.BLUE + "Enter the operation (+, -, *, /, %, **, &, |, ^): " + Colors.ENDC)

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
            elif operation == '%':
                result = num1 % num2
                print(Colors.GREEN + f"The result of {num1} % {num2} is: {result}" + Colors.ENDC)
            elif operation == '**':
                result = num1 ** num2
                print(Colors.GREEN + f"The result of {num1} ** {num2} is: {result}" + Colors.ENDC)
            elif operation in ['&', '|', '^']:
                # Bitwise operations require integers
                if num1.is_integer() and num2.is_integer():
                    int1, int2 = int(num1), int(num2)
                    if operation == '&':
                        result = int1 & int2
                        print(Colors.GREEN + f"The result of {int1} & {int2} is: {result}" + Colors.ENDC)
                    elif operation == '|':
                        result = int1 | int2
                        print(Colors.GREEN + f"The result of {int1} | {int2} is: {result}" + Colors.ENDC)
                    elif operation == '^':
                        result = int1 ^ int2
                        print(Colors.GREEN + f"The result of {int1} ^ {int2} is: {result}" + Colors.ENDC)
                else:
                    print(Colors.RED + "Error: Bitwise operations require integer inputs." + Colors.ENDC)
            else:
                print(Colors.RED + "Invalid operation selected. Please choose a valid operation." + Colors.ENDC)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter numeric values." + Colors.ENDC)
        
        # Ask the user if they want to perform another operation or quit
        choice = input(Colors.BOLD + Colors.YELLOW + "\nWould you like to perform another operation? (yes/y to continue, any other key to quit): " + Colors.ENDC)
        choices = ['yes','y']
        if choice.lower() not in choices :
            print(Colors.BLUE + "Thank you for using the calculator. Goodbye!" + Colors.ENDC)
            break

# Run the calculator
if __name__ == '__main__':
    calculator()

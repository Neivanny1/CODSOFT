#!/usr/bin/python3

'''
Simple Calculator with ASCII Banner and Colors
'''

'''
ANSI color codes
'''
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

'''
ASCII banner
'''
BANNER ='''
                                                          
  ,ad8888ba,         db         88           ,ad8888ba,   
 d8"'    `"8b       d88b        88          d8"'    `"8b  
d8'                d8'`8b       88         d8'            
88                d8'  `8b      88         88             
88               d8YaaaaY8b     88         88             
Y8,             d8""""""""8b    88         Y8,            
 Y8a.    .a8P  d8'        `8b   88          Y8a.    .a8P  
  `"Y8888Y"'  d8'          `8b  88888888888  `"Y8888Y"'   
                                                          
                                                          
'''
def print_banner():
    print(Colors.GREEN + Colors.BOLD)
    print(BANNER)
    print(Colors.ENDC)
'''
Bitwise handler
Takes in 3 arguments: operation, int num1 and int num2
'''
def bitwiseHandler(num1, num2, operation):
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

  

"""
Calculator function
"""
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
        
        '''
        Get user inputs
        '''
        try:
            num1 = float(input(Colors.BOLD + "\nEnter the first number: " + Colors.ENDC))
            num2 = float(input(Colors.BOLD + "Enter the second number: " + Colors.ENDC))
            operation = input(Colors.BLUE + "Enter the operation (+, -, *, /, %, **, &, |, ^): " + Colors.ENDC)

            '''
            Performs calculation based on chosen operation
            '''
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
                # Calls bitwise handler
                bitwiseHandler(num1, num2, operation)
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

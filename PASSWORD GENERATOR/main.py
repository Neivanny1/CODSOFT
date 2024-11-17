#!/usr/bin/python3
'''
PASSWORD GENERATOR
'''
import random
import string

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
Define character sets for password complexity
'''
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = string.punctuation
MINI_PASS_LENGTH = 8
'''
Get user input for password length
'''
def gets_userInput():
    while True:
        try:
            length = int(input(Colors.GREEN + "Enter the password length (minimum 8 characters): "))
            if length >= 8 and length <= 256:
                break
            if length > 256:
                print(Colors.RED + 'Password to big size not supported. Try again.')
            elif length < 8:
                print(Colors.RED + "Password length must be at least 8 characters for security. Try again.")
            else:
                print(Colors.RED + "Invalid input. Please enter a valid number." ) 
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter a valid number." ) 
    return length

'''
gets user choice for complexity
'''
def gets_userChoice():
    print(Colors.HEADER + "\nChoose password complexity:" + Colors.ENDC)
    print(Colors.YELLOW + "1. Lowercase letters only")
    print("2. Lowercase and Uppercase letters")
    print("3. Letters and Digits")
    print("4. Letters, Digits, and Special Characters" + Colors.ENDC)
    while True:
        try:
            # Prompt user for input
            choice = int(input(Colors.BLUE + "Enter your choice (1-4): " + Colors.ENDC))
            # Check if the choice is valid
            if choice in [1, 2, 3, 4]:
                break
            else:
                print(Colors.RED + "Invalid choice. Please select a number between 1 and 4." + Colors.ENDC)
        except ValueError:
            # Handle non-integer input
            print(Colors.RED + "Invalid input. Please enter a valid number (1-4)." + Colors.ENDC)
    return choice


'''
Build the character pool based on user choice
'''
def build_char_pool():
    choice = gets_userChoice()
    if choice == 1:
        char_pool = LOWERCASE
    elif choice == 2:
        char_pool = LOWERCASE + UPPERCASE
    elif choice == 3:
        char_pool = LOWERCASE + UPPERCASE + DIGITS
    elif choice == 4:
        char_pool = LOWERCASE + UPPERCASE + DIGITS + SPECIAL_CHARS
    return char_pool
    
'''
generates passwords
'''
def generate_password():
    # Generate password
    length = gets_userInput()
    char_pool = build_char_pool()
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print(Colors.GREEN + f"\nGenerated Password: {password}" + Colors.ENDC)
    return password

'''
ASCII banner
'''
BANNER = '''
                                                                                                                          
88888888ba      db         ad88888ba    ad88888ba   I8,        8        ,8I   ,ad8888ba,    88888888ba   88888888ba,      
88      "8b    d88b       d8"     "8b  d8"     "8b  `8b       d8b       d8'  d8"'    `"8b   88      "8b  88      `"8b     
88      ,8P   d8'`8b      Y8,          Y8,           "8,     ,8"8,     ,8"  d8'        `8b  88      ,8P  88        `8b    
88aaaaaa8P'  d8'  `8b     `Y8aaaaa,    `Y8aaaaa,      Y8     8P Y8     8P   88          88  88aaaaaa8P'  88         88    
88""""""'   d8YaaaaY8b      `"""""8b,    `"""""8b,    `8b   d8' `8b   d8'   88          88  88""""88'    88         88    
88         d8""""""""8b           `8b          `8b     `8a a8'   `8a a8'    Y8,        ,8P  88    `8b    88         8P    
88        d8'        `8b  Y8a     a8P  Y8a     a8P      `8a8'     `8a8'      Y8a.    .a8P   88     `8b   88      .a8P     
88,ad8888ba,   88888888888 "888b88P"  88"Y88888888888  88888888ba  `8'     db `"Y8888888888888 ,ad8888ba,888888888888ba   
 d8"'    `"8b  88           8888b     88  88           88      "8b        d88b        88      d8"'    `"8b   88      "8b  
d8'            88           88 `8b    88  88           88      ,8P       d8'`8b       88     d8'        `8b  88      ,8P  
88             88aaaaa      88  `8b   88  88aaaaa      88aaaaaa8P'      d8'  `8b      88     88          88  88aaaaaa8P'  
88      88888  88"""""      88   `8b  88  88"""""      88""""88'       d8YaaaaY8b     88     88          88  88""""88'    
Y8,        88  88           88    `8b 88  88           88    `8b      d8""""""""8b    88     Y8,        ,8P  88    `8b    
 Y8a.    .a88  88           88     `8888  88           88     `8b    d8'        `8b   88      Y8a.    .a8P   88     `8b   
  `"Y88888P"   88888888888  88      `888  88888888888  88      `8b  d8'          `8b  88       `"Y8888Y"'    88      `8b  
                                                                                                                          
                                                                                                                          
'''

def print_banner():
    print(Colors.GREEN + Colors.BOLD)
    print(BANNER)
    print(Colors.ENDC)

def main():
    print_banner()
    print( Colors.BLUE + "Welcome to the Password Generator!")
    generate_password()

'''
Run the password generator
'''
if __name__ == "__main__":
    main()

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

def main():
    print( Colors.GREEN + "Welcome to the Password Generator!")
    generate_password()

'''
Run the password generator
'''
if __name__ == "__main__":
    main()

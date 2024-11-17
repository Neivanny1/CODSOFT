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
            length = int(input("Enter the password length (minimum 8 characters): "))
            if length >= 8 and length <= 256:
                print(length)
                break
            elif length > 256:
                print('Password to big size not supported')
            else:
                print("Password length must be at least 8 characters for security. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")  
    return length
'''
gets user choice for complexity
'''
def gets_userChoice():
    print("\nChoose password complexity:")
    print("1. Lowercase letters only")
    print("2. Lowercase and Uppercase letters")
    print("3. Letters and Digits")
    print("4. Letters, Digits, and Special Characters")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in range(1,5):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice. Please enter a valid option (1-4).")
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
    print(f"\nGenerated Password: {password}")

def main():
    print("Welcome to the Password Generator!")
    generate_password()

'''
Run the password generator
'''
if __name__ == "__main__":
    main()
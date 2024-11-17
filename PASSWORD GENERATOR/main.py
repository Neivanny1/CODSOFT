import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    try:
        length = int(input("Enter the desired password length (minimum 6 characters): "))
        if length < 6:
            print("Password length must be at least 6 characters for security. Try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Define character sets for password complexity
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    print("\nChoose password complexity:")
    print("1. Lowercase letters only")
    print("2. Lowercase and Uppercase letters")
    print("3. Letters and Digits")
    print("4. Letters, Digits, and Special Characters")

    # Get user choice for complexity
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    # Build the character pool based on user choice
    if choice == 1:
        char_pool = lowercase
    elif choice == 2:
        char_pool = lowercase + uppercase
    elif choice == 3:
        char_pool = lowercase + uppercase + digits
    elif choice == 4:
        char_pool = lowercase + uppercase + digits + special_chars
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
        return

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print(f"\nGenerated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    generate_password()

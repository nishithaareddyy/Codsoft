import random
import string

print("Welcome to the Password Generator!")

# Ask for password length
length = int(input("Enter the desired password length: "))

# Ask which types of characters to include
use_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower() == "y"
use_lower = input("Include lowercase letters (a-z)? (y/n): ").lower() == "y"
use_digits = input("Include numbers (0-9)? (y/n): ").lower() == "y"
use_symbols = input("Include symbols (!@#$)? (y/n): ").lower() == "y"

# Build the character pool
characters = ""
if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# Check if user selected at least one option
if not characters:
    print(" You must select at least one character type!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"\nYour generated password is: {password}")
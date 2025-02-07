import random
import string


def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    
    if not all_chars:
        print("Error: Please select at least one character type!")
        return None
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

length = int(input("How long should the password be? "))
use_uppercase = input("Should it include uppercase letters? (yes/no): ").strip().lower() == 'yes'
use_numbers = input("Should it include numbers? (yes/no): ").strip().lower() == 'yes'
use_special_chars = input("Should it include special characters? (yes/no): ").strip().lower() == 'yes'

password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
if password:
    print(f"Here is your secure password: {password}")

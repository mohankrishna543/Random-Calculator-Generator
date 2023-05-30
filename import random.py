import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True,
                      include_numbers=True, include_symbols=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 4:
        print("Length should be at least 4.")
        return None

    if len(characters) == 0:
        print("At least one character type should be selected.")
        return None

    password = random.choices(characters, k=length-3)
    password.extend(random.choices(string.ascii_uppercase, k=1))
    password.extend(random.choices(string.ascii_lowercase, k=1))
    password.extend(random.choices(string.digits, k=1))
    password.extend(random.choices(string.punctuation, k=1))
    random.shuffle(password)
    return ''.join(password)

# Example usage
password_length = int(input("Enter the desired length of the password: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

generated_password = generate_password(password_length, include_uppercase,
                                       include_lowercase, include_numbers,
                                       include_symbols)

if generated_password:
    print("Generated password:", generated_password)


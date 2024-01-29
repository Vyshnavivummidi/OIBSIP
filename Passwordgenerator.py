import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Select at least one character set (letters, numbers, symbols).")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Simple Password Generator")

    # User preferences
    length = int(input("Password length: "))
    letters = input("Include letters? (yes/no): ").lower() == 'yes'
    numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Generate and print password
    password = generate_password(length, letters, numbers, symbols)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

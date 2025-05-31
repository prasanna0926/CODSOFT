import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for complexity.")
        return None

    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()"

    # Ensure password has at least one character from each set
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all sets combined
    all_chars = uppercase + lowercase + digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle the result to avoid predictable sequences
    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    try:
        length = int(input("Enter desired password length (minimum 4): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

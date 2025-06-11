import random
import string

def password_generator(length=8):
    # Define character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    spl_chars = string.punctuation    # Special characters

    # Combine all characters
    all_chars = letters + digits + spl_chars

    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(spl_chars)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", password_generator(8))

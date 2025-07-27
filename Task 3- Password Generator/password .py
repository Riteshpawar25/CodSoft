import random
import string

# Prompt the user for password length
length = int(input("Enter the desired password length: "))

# Define character sets (you can modify as per complexity needed)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)  
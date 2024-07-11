import string
import random

# Store all characters in lists
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuations = list(string.punctuation)

# Ask user about the number of characters
while True:
    try:
        characters_number = int(input("How many characters do you want in your password? "))
        if characters_number < 8:
            print("Your password should be at least 8 characters long.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Calculate number of characters for each category
num_lower = round(characters_number * 0.3)
num_upper = round(characters_number * 0.3)
num_digits = round(characters_number * 0.2)
num_punctuations = round(characters_number * 0.2)

# Ensure total number of characters equals the user-specified number
total_chars = num_lower + num_upper + num_digits + num_punctuations
while total_chars < characters_number:
    if num_lower + num_upper + num_digits + num_punctuations < characters_number:
        num_lower += 1
    total_chars = num_lower + num_upper + num_digits + num_punctuations

# Generate password
password_chars = (
    random.sample(lowercase, num_lower) +
    random.sample(uppercase, num_upper) +
    random.sample(digits, num_digits) +
    random.sample(punctuations, num_punctuations)
)

# Shuffle the resulting password characters
random.shuffle(password_chars)

# Join and display the result
password = ''.join(password_chars)
print("Strong Password: ", password)

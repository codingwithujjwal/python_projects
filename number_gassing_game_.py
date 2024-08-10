
# Generate random number

import random 

# define range and max_attempts
Start_number = int ( input(" Enter start number: \n")) # User input Start_number
End_number = int ( input (" Enter end number number: \n ")) # User input End_number
max_attempts = 10 # Here declare user have how many attempts

# generate the secret number
secret_number = random.randint(Start_number, End_number)


# Get the user's guess
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {Start_number} and {End_number}: "))
            if Start_number <= guess <= End_number:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
           

# Validate guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

# track the number of attempts, detect if the game is over
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()

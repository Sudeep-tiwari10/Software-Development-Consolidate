import random  # Importing random to generate random numbers

def number_guessing_game():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")
    print("Keep guessing until you find the correct number!")

    attempts = 0  # To count the number of attempts

    # Start a loop that continues until the correct number is guessed
    while True:
        guess = int(input("Enter your guess: "))  # Assume user enters a valid integer
        attempts += 1  # Increment the attempts count

        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
            break  # Exit the loop when guessed correctly
        elif guess < target_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")

# Start the game
number_guessing_game()

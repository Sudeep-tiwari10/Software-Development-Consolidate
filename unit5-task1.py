""" Number Guessing Game - This game will ask the user to guess a random number between 1 and 10.
The game will provide hints if the guess is too high or too low."""

import random   # Importing the random module for generating random numbers
import sys      # Importing sys to handle system-related functions

def main():
    """
    Main function to run the Number Guessing Game.
    This function initializes the game, generates a random target number,
    and manages the main game loop where the user enters guesses.
    """
    # Generate a random target number between 1 and 10
    target_number = random.randint(1, 10)
    
    # Initialize the number of guesses
    attempts = 0
    
    # Start the game loop
    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess (between 1 and 10): "))
            attempts += 1  # Increment attempt count each round
            
            # Check if the guess is correct, too high, or too low
            if guess == target_number:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif guess < target_number:
                print("Your guess is too low. Try again!")
            else:
                print("Your guess is too high. Try again!")
        
        except ValueError:
            # Handle invalid inputs (non-integer values)
            print("Invalid input! Please enter an integer.")
        
        except KeyboardInterrupt:
            # Handle user interruption gracefully
            print("\nGame interrupted. Exiting...")
            sys.exit()

# Call the main function to start the game
if __name__ == "__main__":
    main()

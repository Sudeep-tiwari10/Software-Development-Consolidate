"""Number Guessing Game - This game prompts the user to guess a randomly generated number between 1 and 10.
It provides hints if the guess is too high or too low. The game also tracks the number of attempts, records the time taken, and saves high scores to a JSON file."""

import random       # To generate a random number for the game
import sys          # To allow graceful exit from the game
import json         # To save and load high scores from a file
import time         # To record the time taken for each game

def main():
    """
    Main function to run the Number Guessing Game.
    
    The function:
    - Generates a random target number between 1 and 10.
    - Manages the main game loop where the user makes guesses.
    - Tracks the number of attempts and time taken.
    - Calls save_high_score() to update high scores if needed.
    """
    # Generate a random target number between 1 and 10
    target_number = random.randint(1, 10)
    
    # Initialize the number of guesses and start the timer
    attempts = 0
    start_time = time.time()
    
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking of between 1 and 10.")
    
    # Main game loop
    while True:
        try:
            # Get user input and validate it as an integer
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt count
            
            # Check if the guess is correct, too high, or too low
            if guess == target_number:
                end_time = time.time()  # Record the end time
                elapsed_time = round(end_time - start_time, 2)  # Calculate time taken
                print(f"Congratulations! You guessed the number in {attempts} attempts and {elapsed_time} seconds.")
                
                # Save the high score
                save_high_score(attempts, elapsed_time)
                break  # Exit the loop when the correct guess is made
            
            elif guess < target_number:
                print("Your guess is too low. Try again!")
            
            else:
                print("Your guess is too high. Try again!")
        
        except ValueError:
            # Handle invalid (non-integer) inputs
            print("Invalid input! Please enter an integer between 1 and 100.")
        
        except KeyboardInterrupt:
            # Handle user interruption gracefully (Ctrl+C)
            print("\nGame interrupted. Exiting...")
            sys.exit()

def save_high_score(attempts, elapsed_time):
    """
    Save the player's score if it's a new high score.
    
    The function:
    - Loads existing high scores from a JSON file.
    - Compares the current score to the saved high score.
    - Updates and saves the score if it's a new record.
    
    Parameters:
    attempts (int): The player's number of attempts to guess correctly.
    elapsed_time (float): The time taken by the player to guess correctly.
    """
    score_file = "high_scores.json"  # Define the high score file path
    
    # Try to load existing scores from file, or initialize if file doesn't exist
    try:
        with open(score_file, 'r') as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = {"high_attempts": None, "best_time": None}
    
    # Check if the current score beats the high score
    new_high_attempts = scores["high_attempts"] is None or attempts < scores["high_attempts"]
    new_best_time = scores["best_time"] is None or elapsed_time < scores["best_time"]
    
    if new_high_attempts:
        scores["high_attempts"] = attempts
        print(f"New record for fewest attempts: {attempts}!")
    
    if new_best_time:
        scores["best_time"] = elapsed_time
        print(f"New record for fastest time: {elapsed_time} seconds!")
    
    # Save the updated scores back to the file
    with open(score_file, 'w') as file:
        json.dump(scores, file)

if __name__ == "__main__":
    # Run the game when the script is executed directly
    main()

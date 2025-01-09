import random


def play_round(user_choice, computer_choice):
    """
    Determines the result of a single round of Rock-Paper-Scissors.

    Parameters:
        user_choice (str): The player's choice ("rock", "paper", or "scissors").
        computer_choice (str): The computer's randomly chosen option.

    Returns:
        str: Result message indicating win, lose, or tie.
    """
    if user_choice == computer_choice:
        return f"Both players selected {user_choice}. It's a tie!"

    # Define win conditions
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if win_conditions[user_choice] == computer_choice:
        return f"{user_choice.capitalize()} beats {computer_choice}! You win!"
    else:
        return f"{computer_choice.capitalize()} beats {user_choice}! You lose."


def rock_paper_scissors():
    """
    Runs the Rock-Paper-Scissors game.
    """
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        # Get user input
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
        possible_choices = ["rock", "paper", "scissors"]

        # Validate input
        if user_choice not in possible_choices:
            print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's choice
        computer_choice = random.choice(possible_choices)
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        # Determine and display the result
        result = play_round(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    rock_paper_scissors()

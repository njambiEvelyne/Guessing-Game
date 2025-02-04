import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get player's choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice not in choices:
            print(f"Invalid choice. Choose from {choices}.")
            continue  # Restart the loop if input is invalid

        # Computer makes a random choice
        computer_selection = random.choice(choices)
        print(f"Computer's choice: {computer_selection}")

        # Check for a tie
        if player_choice == computer_selection:
            print("It's a tie!")
        
        # Check if the player wins
        elif (player_choice == "rock" and computer_selection == "scissors") or \
             (player_choice == "paper" and computer_selection == "rock") or \
             (player_choice == "scissors" and computer_selection == "paper"):
            print("You win!")
        
        # If it's not a tie and the player didn't win, they must have lost
        else:
            print("You lose!")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break

# Run the game
rock_paper_scissor()

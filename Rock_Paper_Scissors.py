import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.")

while True:
    # Get the user's choice
    user_choice = input("Enter your choice: ").lower()
    
    # Check if the user wants to quit
    if user_choice == "exit":
        print("Thanks for playing! Goodbye!")
        break
    
    # Validate the user's choice
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    
    print(f"The computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

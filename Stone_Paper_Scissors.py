import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win!")
            user_score += 1
        else:
            print("Result: Computer wins!")
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break
        round_number += 1

# Start the game
print("Welcome to Rock, Paper, Scissors Game!")
play_game()

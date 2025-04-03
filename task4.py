import random

def get_winner(user, computer):
    if user == computer:
        return "TIE"
    elif (user == "ROCK" and computer == "SCISSORS") or \
         (user == "SCISSORS" and computer == "PAPER") or \
         (user == "PAPER" and computer == "ROCK"):
        return "USER"
    else:
        return "COMPUTER"

user_score = 0
computer_score = 0

print("\nWelcome to Rock, Paper, Scissors! 🎮")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to exit the game.\n")

while True:

    user_input = input("Enter your choice (rock, paper, scissors or quit): ").strip().upper()


    if user_input == "QUIT":
        print("\nGAME OVER!")
        print(f"FINAL SCORE: You {user_score} | Computer {computer_score}")
        print("Thanks for playing! 😊")
        break


    valid_choices = ["ROCK", "PAPER", "SCISSORS"]
    if user_input not in valid_choices:
        print("Invalid choice. Please enter rock, paper, or scissors.\n")
        continue
    computer_choice = random.choice(valid_choices)
    print(f"\nYou chose: {user_input}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    winner = get_winner(user_input, computer_choice)

    if winner == "TIE":
        print("😅 It's a tie!")
    elif winner == "USER":
        print("You win this round!")
        user_score += 1
    else:
        print("😞 You lost this round!")
        computer_score += 1

    print(f"\nSCORE: You {user_score} | Computer {computer_score}\n")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\nFINAL SCORE:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! 😊")
        break

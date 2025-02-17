import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Choose: rock, paper, or scissors")
        
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score - You:", user_score, "Computer:", computer_score)
            break

if __name__ == "__main__":
    play_game()

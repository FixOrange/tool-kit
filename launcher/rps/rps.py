import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play():
    print("=== Rock Paper Scissors ===")
    print("Type: rock, paper, or scissors")

    while True:
        player = input("Your choice: ").lower()

        if player not in choices:
            print("Invalid choice!")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)

        if result == "win":
            print("🎉 You win!")
        elif result == "lose":
            print("💀 You lose!")
        else:
            print("🤝 It's a draw!")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    play()
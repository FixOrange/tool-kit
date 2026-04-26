import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("=== Guess the Number Game ===")
    print("I'm thinking of a number between 1 and 100")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 You guessed it in {attempts} attempts!")
            break

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()

        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
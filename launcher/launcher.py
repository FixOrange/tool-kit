import os

def run_script(path):
    os.system(f'python "{path}"')

def main():
    while True:
        print("\n=== My Tools Launcher ===")
        print("1 - Currency Converter")
        print("2 - Guess Number")
        print("3 - Password Checker")
        print("4 - Rock Paper Scissors")
        print("5 - Website Response Checker")
        print("0 - Exit")

        choice = input("Select: ")

        if choice == "1":
            run_script("currency-converter/main.py")

        elif choice == "2":
            run_script("guess-number/guess_number.py")

        elif choice == "3":
            run_script("password-strength-checker/password_checker.py")

        elif choice == "4":
            run_script("rps/rps_game.py")

        elif choice == "5":
            run_script("website-response-timer/response_checker.py")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
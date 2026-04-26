import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    return score

def main():
    print("=== Password Strength Checker ===")

    while True:
        password = input("\nEnter password (or 'exit'): ")

        if password.lower() == "exit":
            print("Goodbye!")
            break

        score = check_password(password)

        if score <= 2:
            print("Weak password ❌")
        elif score <= 4:
            print("Medium password ⚠️")
        else:
            print("Strong password ✅")

if __name__ == "__main__":
    main()
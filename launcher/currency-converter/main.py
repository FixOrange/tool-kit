import requests

def get_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if to_currency not in data["rates"]:
        return None

    return data["rates"][to_currency]

def convert():
    print("=== Currency Converter ===")

    from_currency = input("From (e.g. USD): ").upper()
    to_currency = input("To (e.g. EUR): ").upper()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return

    rate = get_rate(from_currency, to_currency)

    if rate is None:
        print("Invalid currency code")
        return

    result = amount * rate
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    convert()
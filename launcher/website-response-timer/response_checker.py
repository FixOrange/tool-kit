import requests
import time

def check_website(url):
    try:
        start = time.time()
        response = requests.get(url)
        end = time.time()

        response_time = (end - start) * 1000
        print(f"{url} → {response.status_code} ({response_time:.2f} ms)")
    except:
        print("Error connecting to site")

def main():
    print("=== Website Response Checker ===")

    while True:
        url = input("\nEnter URL (or 'exit'): ")

        if url.lower() == "exit":
            print("Goodbye!")
            break

        check_website(url)

if __name__ == "__main__":
    main()
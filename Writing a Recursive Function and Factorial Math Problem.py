# This script prints a welcome message, asks the user to enter an integer, and computes the factorial using recursion

# This prompts the user for a valid integer within the specified range and repeats until a correct entry is given
def ask_for_int(low, high):
    while True:
        try:
            num = int(input(f"Enter an integer between {low} and {high}: "))
            if low <= num <= high:
                return num
            print("Out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# This recursively calculates a factorial by multiplying n by the factorial of n minus one, with zero or one as the base case
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# This is a main program logic that repeatedly gets input, calculates the factorial, and shows the result
def main():
    print("Recursive Factorial Calculator")

    while True:
        n = ask_for_int(0, 996)
        print(f"{n}! = {factorial(n)}")

        if input("Another? (yes/no): ").strip().lower() != "yes":
            break

    print("Goodbye!")

# This ensures the main() function runs only when the script is executed directly, not when imported
if __name__ == "__main__":
    main()
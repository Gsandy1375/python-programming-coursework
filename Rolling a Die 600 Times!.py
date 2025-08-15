# This script simulates rolling a 6-sided die 600 times and counts the outcomes for each side of the die

# This allows the generation of random numbers
import random

def main():
    # This creates a list of 6 counters initialized to 0
    counters = [0] * 6

    # This simulates rolling a 6-sided die exactly 600 times
    num_rolls = 600
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        counters[roll - 1] += 1  # Adjust index (1–6 → 0–5)

    # This prints the results using a loop
    for i in range(6):
        side = i + 1
        count = counters[i]
        percentage = count / num_rolls
        print(f"Num of times {side} was rolled {count}")
        print(f"Percentage is {percentage}")

    print("Goodbye")

# This runs he program
if __name__ == "__main__":
    main()

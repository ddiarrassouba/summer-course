import random

with open("random_numbers.txt", "w") as file:
    for _ in range(100):
        file.write(f"{random.randint(50, 100)}\n")

print("Wrote 100 random integers to random_numbers.txt")

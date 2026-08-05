#------------------------------------ Pre problems set -----------------------------------------------------
# Write a Python Script that writes 100 random integer values (from 1 to 1000) to another file (.txt) .  
# **Only do this once**

# import random

# with open("random_numbers.txt", "w") as file:
#     for _ in range(100):
#         file.write(f"{random.randint(1, 1000)}\n")

# print("Wrote 100 random integers to random_numbers.txt")


# Write another Python Script that opens that file, displays the highest number in the list, 
# the lowest number in the list, and the average of that list.

# with open("random_numbers.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file if line.strip()]

#     new_list = []
#     for line in lines:
#         line  = line.strip()
#         line = int(line)
#         new_list.append(line)
#     print(new_list)

#     lines_stripped = [int(line.strip())]

# if numbers:
#     highest = max(numbers)
#     lowest = min(numbers)
#     average = sum(numbers) / len(numbers)

#     print(f"Highest number: {highest}")
#     print(f"Lowest number: {lowest}")
#     print(f"Average: {average}")
# else:
#     print("The file is empty.")



#----------------------------------- Exercices ------------------------------------------------------------
# Randomly assign a number from 1 to 100.

# Write a block of code that takes in user input until they guess the random number

# Prompt the user to help them with their guess
# Handle the following situations:
# User does not input the right python data type
# User inputs a negative number
# User inputs a number outside the guess range
# Hint: use random.randomint() to generate a random number

import random

secret_number = random.randint(1, 100)

print("I have chosen a number between 1 and 100. Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < 0:
        print("Please enter a positive number.")
    elif guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        break

# ------------------------------ Exercice 3 ----------------------------------------------------------
# Given a list of numbers, write a program that:

# Loops through the List: [10, -5, 20, ‘hello’, 5.2, 15, None, 30]

# Skips any None values or non-integer types with an error message using try/except
# Raises a ValueError if it finds a negative number (stops the program)

# Collects all valid positive integers into a new list

# Prints the new list and the sum of its numbers

# Once you have a solution, remove -5 from the list and run it again.

# Hints:  
# Use isinstance(item, int) to check types
# Build the valid list as you go

items = [10, -5, 20, 'hello', 5.2, 15, None, 30]
valid_number = []

import random

# Step 1: Choose a random number from 1 to 100
secret_number = random.randint(1, 100)

# Step 2: Give the user instructions
print("I have chosen a number between 1 and 100. Try to guess it!")

# Step 3: Keep asking until the user guesses correctly
while True:
    # Step 4: Ask for user input
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        # Step 5: Handle invalid input
        print("Please enter a valid integer.")
        continue

    # Step 6: Check for negative numbers
    if guess < 0:
        print("Please enter a positive number.")
    # Step 7: Check if the number is outside the allowed range
    elif guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
    # Step 8: Give hints for too low or too high guesses
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    # Step 9: End the game when the guess is correct
    else:
        print("Correct! You guessed the number.")
        break
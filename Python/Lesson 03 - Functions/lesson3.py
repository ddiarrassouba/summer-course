# Print the number from 1 to 100. if the number is divisible by 3, print "Fizz" instead of the number. If the number is divisible by 5, print "Buzz" instead of the number. If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If it is divsi by 5, print "Buzz" instead of the number. If it is divisible by both, print "FizzBuzz" instead of the number.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

#----------------------- Problem 2 -----------------------
# ask the user for "rock", "paper", or "scissors". Then randomly generate a choice for the computer's choice of "rock", "paper", or "scissors". Display whether the user won, lost, or tied.
# for user in ["rock", "paper", "scissors"]:
#     import random
#     computer = random.choice(["rock", "paper", "scissors"])
#     print(f"User choice: {user}")
#     print(f"Computer choice: {computer}")

#     if user == computer:
#         print("It's a tie!")
#     elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
#         print("You win!")
#     else:
#         print("You lose!")

#----------------------- Problem 3 -----------------------
# Create a guess game. Randomly assign a number from 1 to 100 (using the random module). Ask the user
# ask the user to guess the number. If the user's guess is higher, print "Too high!". If the user guesses lower, print "Too low!".  and exit the program. The user should be able to keep guessing until they get it right.
# display to the user how many guesses they have made. If the user guesses the number correctly, print "Congratulations! You guessed the number." and exit the program.
# import random
# number = random.randint(1, 100) 
# guesses = 0
# for i in range(1, 101):
#     guess = int(input("Guess a number between 1 and 100: "))
#     guesses += 1
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the number.")
#         print(f"You made {guesses} guesses.")           
#         break                                                                                                               

#--------------------------- FUNCTIONS RANDOM NUMBERS ----------------------
# write a python script that randomly generates a number between 1 and 100.
# if the number is less than 50, state "The number is less than 50". If the number is greater than 50, state "The number is greater than 50". If the number is equal to 50, state "The number is equal to 50".
# import random

# number = random.randint(1, 100)
# print(f"Generated number: {number}")

# if number < 50:
#     print("The number is less than 50")
# elif number > 50:
#     print("The number is greater than 50")
# else:
#     print("The number is equal to 50")

# print(f"Random number: {number}")

#--------------------------- user defined functions ----------------------
# Write a function that takes two numbers as arguments and returns their sum. Then, call the function with two numbers and print the result.
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 10)
# print(f"The sum is: {result}")  

#--------------------------- user defined functions ----------------------
# write a python function that calculates and returns the area  of rectangle using two integer inputs from the user! Outside of the function call, print the area.
# def rect_area(length, width):
#     return length * width

# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))
# area = rect_area(length, width)
# print(f"The area of the rectangle is: {area}")  

# ------------------------------- TRY IT YOURSELF -------------------------------
# write a function called tip() that has two parameters named total and percentage
# This function should return the amount of you should tip given a total and the percentage you want to tip.
# print the amount returned outside of the function call.

# def tip(total, percentage):
#     return total * percentage / 100

# total = float(input("Enter the total amount: "))
# percentage = float(input("Enter the tip percentage: "))
# amount = tip(total, percentage)
# print(f"The tip amount is: {amount}")   

#------------------------------- TRY IT YOURSELF -------------------------------
# write a function that is called "has_more_characters", This function should accept two strings as arguments, and will return the string that has more characters.
# Outside of the function call, print the string with more characters.

# def has_more_characters(str1, str2):
#     if len(str1) > len(str2):
#         return str1
#     elif len(str2) > len(str1):
#         return str2
#     else:
#         return "Both strings have the same number of characters."   
    

# result = has_more_characters("stringa", "stri2")
# print(result)

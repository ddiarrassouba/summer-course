# age = 20
# money = 100
# isMilitary = True
# inOnPermanent = False
# syntax: if condition:
# if condition:
     # code block
#  else:
     # code block

#Example 1
# if money > 50:
# score = 89
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# # Example 2
# score = 50
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")   

#-------------------------------- TRY IT YOURSELF --------------------------------
#write a script that asks a user for a number. The script then checks the number and prints
# "positive", "zero", or "negative" depending on the number.

# number = float(input("Please enter a number: "))
# if number > 0:
#     print("positive")
# elif number == 0:
#     print("zero")
# else:
#     print("negative")

#--------------------------- Hands-on Exercise 1 ---------------------------
# Write a Python Script that asks a user for an integer number, and then checks if the number is positive using an if statement
# Check: Should print "The number is positive" if the number is greater than 0.
# number = int(input("Please enter an integer number: "))
# if number > 0:
#     print("The number is positive")


#--------------------------- Hands-on Exercise 2 Event Or Odd ---------------------------
# Write a Python script that asks a user for an integer number. Check if the number is even or odd using if and else.
# Check: Should print "Even" or "Odd" based on the number.
# number = int(input("Please enter an integer number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# --------------------------- Hands-on Exercise 3 Age Category ---------------------------
# Write a python script that asks a user for their age, and then uses if, elif, and else to print the 
# correct category for the person by based on their age.
# Under 13: "Child"
# 13-19: "Teenager"
# 20-64: "Adult"
# 65+: "Senior"
# Check: Should print the correct category based on age

# age = int(input("Please enter your age: "))
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

#---------------------------- Hands-on Exercise 4 Compare Two Numbers -------
# Write a Python Script that asks a user for two numbers. Compare the two numbers and print which is larger, or if they're equal.---------------------------
# Check: Should print "{first_number} is larger", "{second_number} is larger", or "The numbers are equal".
# a = 10
# b = 20
# if a > b:
#     print(f"{a} is larger than {b}")
# elif b > a:
#     print(f"{b} is larger than {a}")
# else:
#     print(f"{a} and {b} are equal")

# ---------------------------- Hands-on Exercise 5 Grade Converter --------------------------
# 90+: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Check: Should print the correct letter grade.

# user_grade = int(input("Please enter your grade: "))
# if user_grade >= 90:
#     print("A")  
# elif user_grade >= 80:
#     print("B")
# elif user_grade >= 70:
#     print("C")
# elif user_grade >= 60:
#     print("D")
# else:
#     print("F")

#---------------------------- LOOPS --------------------------
#ask the user to input an even integer number. If the user inputs an odd number, the program should print "That's not an even number!" and ask for another input. This should continue until the user inputs an odd number. Once the user inputs an even number, the program should print "Thank you!" and exit.
# while True:
#     number = int(input("Please enter an even integer number: "))
#     if number % 2 == 0:
#         print("Thank you!")
#         break
#     else:
#         print("That's not an even number!")

#----------------------------Try it yourself--------------------------
secret_number = 22

user_guess = int(input("Guess an integer number: "))
count = 0
while user_guess != secret_number:
    if user_guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
    user_guess = int(input("Guess an integer number: "))
    count += 1

print(f"Congratulations! You guessed the correct number, {user_guess}.") 
print(f"It took you {count} attempts to guess the correct number.")   
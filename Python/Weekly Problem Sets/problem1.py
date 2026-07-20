# Write a program that asks the user for their **name** and their **favorite number**, then prints a personalized card using `print()`.
# **Requirements:**
# - Use `input()` to collect the name and favorite number
# - Use `print()` to display the card with a border made of `*` characters
# - The border of '*' characters should always be based on the length of the favorite number 
# problem - Personalized Card
# Get the users name
# user_name = input("Please enter your name: ")
# # Get the users favorite number 
# user_number = int(input("Please enter your favorite number: "))

# # Define a function to create the personalized card based on the user's input.
# def personalized_card(name, number):
#     # Create the sentences for the card
#     sentence1 = f"Hello, {name}!"
#     sentence2 = f"Your favorite number is {number}."
    
#     # Determine the length of the longest sentence
#     max_length = max(len(sentence1), len(sentence2))
    
#     # Create the border based on the longest sentence
#     border = '*' * (max_length + 4)  # Adding 4 for padding
    
#     # Print the card
#     print(border)
#     print(f"* {sentence1.ljust(max_length)} *")
#     print(f"* {sentence2.ljust(max_length)} *")
#     print(border)   
# # inside of the function, create both sentences.
# name = "Hello, " + user_name
# # take the length of both, and compare them. The longest sentence is going to drive the size of the border.
# # create the card based on that.
# # print out the card..

# name = input("what is your name?")
# favorite_number = input("what is your favorite number?")

# card_width = 46
# inside_width = card_width - 2

# message1 = f"Afrjigi, {name}!"
# message2 = f"Your favorite number is {favorite_number}"

# formatted_message1 = message1.ljust(inside_width - 2)
# formatted_message2 = message2.ljust(inside_width - 2)

# border = "*" * card_width

# print(border)
# print(f"*{formatted_message1}*")
# print(f"*{formatted_message2}*")
# print(border)

# from pyexpat.errors import messages


# name = input("what is your name?")
# favorite_number = input("what is your favorite number?")

# card_width = 46
# inside_width = card_width - 2

# message = [f"Afrjigi, {name}!", f"Your favorite number is {favorite_number}"]

# border = "*" * card_width

# print(border)
# for message in messages:
#     print(f"*  {message.ljust(inside_width - 2)}*")
# print(border)

#-----------------------------Problem set 2----------------------------------------
# ## Problem 2 — Sequence Explorer

# Use `range()` to print each of the following sequences. Each sequence should be printed on a single line, with values separated by spaces.

# # 1. All integers from **1 to 15** (inclusive)
# def print_sequence(start: int, end: int, step: int = 1) -> None:    

#     for i in range(start, end + 1, step ):
#         print(i, end=' ')
#     print()  
# # for a new line after the sequence

# # 2. All **even** numbers from **2 to 30** (inclusive)

# print_sequence(2, 30, 2)    

    
# # 3. A **countdown** from **20 down to 0**, counting by 2s

# print_sequence(20, 0, -2)  

# print() 
# print(1,2,3,4)   
# # for a new line after the sequence    

# # **Example output for sequence 1:**

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

## Problem 4 — Road Trip Fuel Calculator

# Write a program that helps a driver estimate the fuel cost for a road trip.

# Ask the user for:
# def road_trip_fuel_calculator():
#     # 1. The **distance** of the trip in miles
#     distance = float(input("Enter the distance of the trip in miles: "))    
#     # 2. Their car's **fuel efficiency** in miles per gallon (MPG)
#     fuel_efficiency = float(input("Enter your car's fuel efficiency in MPG: "))
#     # 3. The current **price of gas** per gallon in dollars
#     gas_price = float(input("Enter the current price of gas per gallon in dollars: "))

#     # Calculate and print:
#     # - The number of gallons needed (rounded to 2 decimal places)
#     gallons_needed = round(distance / fuel_efficiency, 2)   
#     # - The total fuel cost (rounded to 2 decimal places)
#     total_fuel_cost = round(gallons_needed * gas_price, 2)

#     print()
#     print("--- Road Trip Fuel Estimate ---")
#     print(f"Distance:        {distance} miles")
#     print(f"Fuel efficiency: {fuel_efficiency} MPG")
#     print(f"Gas price:       ${gas_price} / gallon")
#     print()
#     print(f"Gallons needed:  {gallons_needed:.2f}")
#     print(f"Total fuel cost: ${total_fuel_cost:.2f}")

# road_trip_fuel_calculator()

# **Example output:**
# ```
# --- Road Trip Fuel Estimate ---
# Distance:        350 miles
# Fuel efficiency: 28 MPG
# Gas price:       $3.45 / gallon


# Gallons needed:  12.5
# Total fuel cost: $43.13
# ```

# **Requirements:**
# - Use `input()` for all three inputs
# - Cast inputs to `float` using `float()`
# - Use `print()` with clear labels for all output values

# **Advanced:**
# Extend the program to also calculate the cost for **3 different gas price scenarios** using `range()`:
# - The price the user entered
# - That price plus $0.50
# - That price plus $1.00

# Print all three estimates in a table. Use `range()` to loop through the three scenarios rather than writing three separate calculations.

# ```
# --- Price Scenarios ---
# Gas @ $3.45/gal:  Total = $43.13
# Gas @ $3.95/gal:  Total = $49.38
# Gas @ $4.45/gal:  Total = $55.63
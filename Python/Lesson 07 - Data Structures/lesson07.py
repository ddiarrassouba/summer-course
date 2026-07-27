#---------------------------- PROBLEM SET 1 DATA STRUCTURE -----------------------------------------------
#You are building a simple database for a military unit. Each soldier has a name, rank, and years of service. 
# Your job is to store this information and write a function that lets the commanding officer quickly look up 
# any soldier's details by their last name.

# Create a dictionary called unit where each key is a soldier's last name and each value is another dictionary '
# 'containing "rank" and "years_of_service“

# Populate it with at least 5 soldiers Write a function lookup_soldier(unit, last_name) that takes the dictionary 
# and a last name and prints the soldier's full profile, or a friendly message if the soldier is not found

# Write a function lookup_soldier(unit, last_name) that takes the dictionary and a last name and prints the 
# soldier's full profile, or a friendly message if the soldier is not found

# Create a dictionary
# unit = {
#     "Johnson": {
#         "name": "Michael Johnson",
#         "rank": "Captain",
#         "years_of_service": 12
#     },
#     "Smith": {
#         "name": "Angela Smith",
#         "rank": "Sergeant",
#         "years_of_service": 8
#     },
#     "Williams": {
#         "name": "David Williams",
#         "rank": "Lieutenant",
#         "years_of_service": 6
#     },
#     "Brown": {
#         "name": "Sophia Brown",
#         "rank": "Corporal",
#         "years_of_service": 4
#     },
#     "Davis": {
#         "name": "Robert Davis",
#         "rank": "Private",
#         "years_of_service": 2
#     }
# }
# # create a lookup function

# def lookup_soldier(unit, last_name):
#     # Format the name so "smith", "SMITH", and "Smith" all work.
#     last_name = last_name.strip().title()

#     if last_name in unit:
#         soldier = unit[last_name]

#         print("Soldier found!")
#         print("Name:", soldier["name"])
#         print("Rank:", soldier["rank"])
#         print("Years of service:", soldier["years_of_service"])
#     else:
#         print("Sorry, no soldier with the last name", last_name, "was found.")

# search_name = input("Enter the soldier's last name: ")
# lookup_soldier(unit, search_name)
#----------------------------------- PROBLEM SET 2 -------------------------------------------------------
# A military base has two lists of personnel — soldiers who are authorized to enter a restricted zone, 
# and soldiers who showed up at the gate today. Your job is to write a function that uses sets to help the security officer quickly answer three questions:

# Who showed up that is authorized? (let them in)
# Who showed up that is not authorized? (turn them away)
# Who is authorized but didn't show up? (report as absent)

# Store the two groups as sets 
# Write a function check_gate(authorized, arrived) that returns all three answers using set operations 
# Print each result clearly

# Starter Code:
authorized = {"Smith", "Johnson", "Williams", "Brown", "Davis"} 

arrived = {"Smith", "Davis", "Williams", "Rodriguez"}

# Find who can enter

authorized_and_arrived = authorized & arrived

# Find who must be turned away

not_authorized = arrived - authorized

# Find who is absent

absent = authorized - arrived

# Create function

def check_gate(authorized, arrived):
    authorized_and_arrived = authorized & arrived
    not_authorized = arrived - authorized
    absent = authorized - arrived

    return authorized_and_arrived, not_authorized, absent

# Call the function

let_in, turn_away, absent = check_gate(authorized, arrived)

# Print answers

print("Let in:", let_in)
print("Turn away:", turn_away)
print("Absent:", absent)


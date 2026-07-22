#---------------------- Manipulation Files -------------------------------------------

# write a python script that write 100 random integers ranging from 50 to 100 into a file.
# Each integers should be on a a separate line.

# Write another Python script that reads from that file, finds the minimum value, maximum value,
# average value of the 100 random integers. Do not use min() or max() function.
# Find a way to get these values without a built_in function

import random


file_name = "random_integers.txt"

with open(file_name, "w") as output_file:
    for _ in range(10):
        random_number = random.randint(50, 100)
        output_file.write(f"{random_number}\n")

print(f"100 random integers were written to {file_name}.")


with open(file_name, "r") as input_file:
    first_number = int(input_file.readline())

    # total = 0
    # max = 0
    # min = 100


    minimum_value = first_number
    maximum_value = first_number
    total = first_number
    count = 1

    for line in input_file:
        number = int(line.strip())

        if number < minimum_value:
            minimum_value = number

        if number > maximum_value:
            maximum_value = number

        total += number
        count += 1

average_value = total / count

print(f"Minimum value: {minimum_value}")
print(f"Maximum value: {maximum_value}")
print(f"Average value: {average_value:.2f}")
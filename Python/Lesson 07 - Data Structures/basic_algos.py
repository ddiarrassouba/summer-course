# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2] # shallow copy (new list)
    list2[0] = "hi"       # modify in place
    list3 = "".join(list2) # creates a new list

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)




# Exercise 2

# What's the difference between sort and sorted?

# Which one is a list method and which one is a function that works on lists?

# Please explain



# Exercise 3

# Write a function that doubles the elements in a list.




# Do you need to return anything here?



# Write a function that doubles the elements in a tuple.



# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions
def my_reserve_two(in_list):
    in_list[index] = in_list[index -1]

def bubble_sort(in_list):
    for start_index in range(len(in_list) - 1):
        left_index = start_index
        for current_index in range(len())

# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)

# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions
def add_tuple(frac_one, frac_two):
    x1, y1 = frac_one
    x2, y2 = frac_two

    return x1 * x2, y1 * y2


# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates

def distance(coord_one, coord_two):
    x1, y1 = coord_one
    x2, y2 = coord_two

    return 

# extension: make it work for more than two dimensions


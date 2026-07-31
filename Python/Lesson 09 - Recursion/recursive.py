# from unittest import result


# def palindrome(input_str):
#     if input_str == "":
#         return True
#     if len(input_str) == 1:
#         return True

#     if input_str[0] != input_str[-1]:
#         return False
#     print(f"computing {input_str[1:-1]}")
#     result = palindrome


# Calculate the sum of a list of numbers using recursion
# import numbers


# def recursive_sum(numbers):
#     if len(numbers) == 0:
#         return 0
# # recursive case

#     return numbers[0] + recursive_sum(numbers[1:])


# values = [2, 4, 6, 8]
# result = recursive_sum(values)

# print(result)

# Multiple recursions

# def fibonacci(number):
#     # Base cases
#     if number == 0:
#         return 0

#     if number == 1:
#         return 1

#     # Two recursive calls
#     return fibonacci(number - 1) + fibonacci(number - 2)


# result = fibonacci(6)
# print(result)

def branches(number):
    if number == 0:
        return

    print(number)

    branches(number - 1)
    branches(number - 1)


branches(2)
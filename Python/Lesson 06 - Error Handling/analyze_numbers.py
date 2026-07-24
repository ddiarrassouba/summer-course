with open("random_numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip()]

if numbers:
    highest = max(numbers)
    lowest = min(numbers)
    average = sum(numbers) / len(numbers)

    print(f"Highest number: {highest}")
    print(f"Lowest number: {lowest}")
    print(f"Average: {average}")
else:
    print("The file is empty.")

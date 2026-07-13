# Write a script that prompts the user for a diameter of the pizza and outputs the area
pizza_diameter = input("what is of the disameter of the pizza")
pizza_diameter = float(pizza_diameter)
area = 3.14 * (pizza_diameter / 2) ** 2
print(area)

#write a script that calculate the price per area. The user should input the diameter and the cost.
pizza_cost = input("what is the cost of the pizza? ")
pizza_cost = float(pizza_cost)
print(pizza_cost)

print(f"The cost per area is {pizza_cost / area:.02f}")



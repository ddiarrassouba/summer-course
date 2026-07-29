#-------------------------- OOPS -----------------------------------------------------------------------------
# ------------------------------ HANDS-ON 1 --------------------------------------------------------------
# ------------------------- Create a spacecraft class -------------------------------------------------------


# Create an empty class
# from turtle import distance


# class Spacecraft:
#     def __init__(self, name, fuel_level, fuel_efficiency):
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency

#     def calculate_fuel_needed(self, distance):
#         return distance / self.fuel_efficiency

#     def travel(self, distance):
#         fuel_needed = self.calculate_fuel_needed(distance)

#         if self.fuel_level >= fuel_needed:
#             self.fuel_level -= fuel_needed
#             print(f"{self.name}, traveled {distance} miles.")
#             print(f"Fuel remaining: {self.fuel_level:.2f}")
#             return True
#         else:
#             print("You do not have enough fuel.")
#             print(f"Fuel needed: {fuel_needed:.2f}")
#             print(f"Fuel available: {self.fuel_level:.2f}")
#             return False

#     def add_fuel(self, amount):
#         if amount > 0:
#             self.fuel_level += amount
#             print(f"Added {amount} unit of fuel.")
#         else:
#             print("Fuel amount must be greater than zero")

#     def display_status(self):
#         print(f"Spacecraft: {self.name}")
#         print(f"Fuel: {self.fuel_level:.2f}")
#         print(f"Fuel Efficiency: {self.fuel_efficiency:.2f}")

# ship1 = Spacecraft("Explorer",100 ,10)
# ship2 = Spacecraft("Exploer", 100, 5)


# # Testing the Spacecraft

# ship.display_status()
# ship.travel(50)
# ship.add_fuel(20)
# ship.display_status()

# ---------------------------------------- Create a planet class -----------------------------------------

# create a planet class

class Planet:
    pass

    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

# create a planet

import math

def __sub__(self, other):

    return math.dist(self.coordinates, other.coordinates)

planets = [
    Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
    Planet("Mars", (227.9, 0.0, 1.0), 1, 20, "Thin"),
    Planet("Jupiter", (778.5, 50.0, 12.0), 3, 40, "Gas Giant"),
    Planet("Saturn", (1434.0, -80.0, -20.0), 2, 35, "Gas Giant"),
    Planet("Uranus", (2871.0, 30.0, 40.0), 2, 45, "Icy"),
    Planet("Neptune", (4495.0, -25.0, 70.0), 4, 50, "Icy"),
    Planet("Pluto", (5906.0, 120.0, -90.0), 5, 60, "Frozen"),
    Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
    Planet("Kepler-22b", (600000.0, 0.0, 0.0), 3, 70, "Earth-like"),
    Planet("Proxima b", (402080.0, 30.0, 10.0), 5, 80, "Unknown")
]


def find_planet(planet_name):
    for planet in planets:
        if planet.name.lower() == planet_name.lower():
            return planet

    return None

        
print(planets[0])
print(planets[1])

for planet in planets:
    print(planet)
    print()


# Overide __str__

def __str__(self):
    return(
        f"Planet:{self.name}\n"
        f"Coordinates: {self.coordinates}\n"
        f"Danger: {self.danger}\n"
        f"Resources: {self.resources}\n"
        f"Atmosphere: {self.atmosphere}\n"
    )

earth = find_planet("Earth")
mars = find_planet("Mars")

print(earth)
print()

earth = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
mars = Planet("Mars", (227.9, 0.0, 1.0), 1, 20, "Thin")

distance = earth - mars
print(f"Distance from Earth to Mars: {distance:.2f}")




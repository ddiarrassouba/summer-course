# ----------------------------------- Problem 1 — Soldier Roster & Dispatch System -----------------------------------------------------------
# **Create a `Soldier` class** with the following:

class Soldier:
    def __init__(self, name, rank, fitness, deployed):
#   - An `__init__` method that accepts `name`, `rank`, `fitness`, and `deployed` parameters
#   - Store these as instance attributes using `self.name`, `self.rank`, `self.fitness`, and `self.deployed`

        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

#   - Add a `dispatch()` method that sets `self.deployed = True`

    def dispatch(self):
        self.deployed = True

#   - Add a `__str__` method that returns a formatted string with the soldier's information (e.g., `"Santos (PRIVATE, fitness: 91, deployed: False)"`)
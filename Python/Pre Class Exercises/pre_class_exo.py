#----------------------------- PRE CLASS PROBLEM -------------------------------------------
# Intelligence analysts have intercepted a transmission from an enemy outpost. The signal contains 100 scrambled numeric values — but buried inside are the true coordinates of the enemy's hidden command center.
# Your commanding officer explains: "The enemy encodes their location by hiding it in plain sight. Take the 5 highest signal values, sum them together, then divide by 10. The result is the target's grid coordinate."
# Your mission: write a Python program to decode the transmission and report the coordinates.  You have 20 minutes to finish this before the enemy moves their command post.

signals = []
with open("preclass_exo_data.txt", "r") as in_file:
    for line in in_file:
        signal = int(line)

        signals.append(int(signal))
signals_sorted = sorted(signals, reverse=True)
high_5 = signals_sorted[:5]
coordinate = sum(high_5) / 10.0
print(f"The coordinate is {coordinate}")

#----------------------------------- Problemn set 1 -------------------------------
# Starting from scratch write a python script that allows you to play rock, paper, scissors against the computer.
# However, in this version you will ask the user how many games they want to play to determine the overall winner.  The computer has other things to do, so it will only accept playing the best of 1 to 9 games.Example:  How many games would you like to play to determine who is the ultimate winner?  Implied:  User input can only be an odd number from 1 to 9.  Continue to ask the user to re-enter how many games they would like to play until the user meets these criteria.  
# Also implied:  If the user wants to play the best of 3 games, and wins the first two, they do not need to play a third game.
# Bonus:  Incorporate ASCII-ART and delays into your game to add some flare.


valid_games_counts = [1, 3, 5, 7, 9]
total




#---------------------------- Problem set 3 -------------------------------------------------

# 3 Let’s make this a function:
# A = P(1 + r/n)**nt

def compound_interest(P, r, n=1,t=10):
    #P is the priciple
    A = P*(1 + r/n) ** (n*t)
    return A

A1 = compound_interest(1000,0061)
A2 = compound_interest(1000,0031)
A3 = compound_interest(1000, )

print(f"A1:02f, A2:02f, A3:02f")

# Takes input from user and calculates area of a circle

import math  # So we can use pi and all its digits


def area(x):
    if x >= 0:
        return x * math.pi
    else:
        print("Can't calculate negative radii")


userInput = int(input("Enter radius: "))
ans = area(userInput)
ansError = "Negative radii cannot be calculated."
if ans < 0:
    print(ansError)
else:
    print(ans)

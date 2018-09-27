from random import *

"""
Third Weekly Challenge:
Given this list [25, 50, 10, 5, 1] of coins find the least amount of coins it would take to give change for.
Example:
201 would be 5 coins because 4 50 cent coins and 1 1 cent coins
23 would be 5 coins because 2 30 cent coins and 3 1 cent coins

"""

def change(n):
    coins = [50, 25, 10, 5, 1]


for i in range(5):
    temp = int(1000*random())
    print(temp, "change =", change(temp))

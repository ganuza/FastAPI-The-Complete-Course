"""
Write Python program to do:
- you have $50
- you buy an item that is $15, taxed at 3%
- print how much money you have left
"""

balance = 50
cost = 15
tax = .03

money_left = balance - (cost * (1 + tax))

print(money_left)
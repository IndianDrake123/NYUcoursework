"""
Author: Brian Thomas 
Assignment / Part: HW3 - Q1 Lemonade Stand Profit Calculator
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

print("Welcome to the Lemonade Stand Profit Calculator!")

season = input("Enter the current season (summer/other): ")
small_cups = float(input("Enter the current number of small cups of lemonade sold: "))
medium_cups = float(input("Enter the current number of medium cups of lemonade sold: "))
large_cups = float(input("Enter the current number of large cups of lemonade sold: "))

if season == 'summer':
    profit = (small_cups * 1) + (medium_cups * 1.25) + (large_cups * 1.5)
else:
    profit = (small_cups * .75) + (medium_cups * 1) + (large_cups * 1.25)

print(profit)
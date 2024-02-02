"""
Author: Brian Thomas 
Assignment / Part: HW3 - Q2 Baby Steps
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

days = int(input("Enter the number of days (1 to 100): "))

while days < 0 or days > 100:
    days = int(input("Enter the number of days (1 to 100): "))

steps = 0
for day in range(1, days + 1):
    steps += (day * 2) - 1

print(steps)
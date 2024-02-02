# Brian
# Lab 1: Test Your Luck  
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

user = int(input("Will the coin land on 0 (Heads) or 1 (Tails)? "))

result = random.randint(0, 1)

print("Coin Flip Result:", result)
print("User guess correctly: True" if result == user else "User guess correctly: False")

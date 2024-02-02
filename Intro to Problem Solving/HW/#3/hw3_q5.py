"""
Author: Brian Thomas 
Assignment / Part: HW3 - Q5 Majestic Hourglass
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

layers = int(input("Please enter a positive integer: "))
stars = layers + 1
for layer in range(layers):
    stars -= 1
    print(' ' * (layers - stars) + ("*" * ((stars * 2) -1)))

for layer in range(layers - 1):
    stars += 1
    print(' ' * (layers - stars) + ("*" * ((stars * 2) -1)))
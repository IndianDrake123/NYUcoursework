"""
Author: Brian Thomas 
Assignment / Part: HW4 - Q3 The Great A-B Swap-a-Thon
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

n = int(input("Enter a positive integer 'n': "))

complete_string = 'A'

for iter in range(1, n + 1):
    print(f"Iteration {iter}: {complete_string}")
    checked = ''
    for check in complete_string:
        if check == 'A':
            checked += 'B'
        if check == 'B':
            checked += 'A'
    complete_string += checked
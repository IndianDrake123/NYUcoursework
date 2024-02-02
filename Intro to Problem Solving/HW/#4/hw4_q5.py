"""
Author: Brian Thomas 
Assignment / Part: HW4 - Q5 Read Between The Lines 
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

encoded_string = input("Enter an encoded string: ")
alpha_string = ''
decoded_string = ''
key = int(input("Enter a key: "))

for char in encoded_string[::-1]:
    if not char.isdigit():
        alpha_string += char

for char in alpha_string[::(key + 1)]:
    decoded_string += char

print(decoded_string)
"""
Author: Brian Thomas 
Assignment / Part: HW3 - Q4 Why, This Car Could Be Systematic, Programmatic, Quadratic!
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))

discriminant = (b ** 2) - (4 * a * c)

if a == 0 and b == 0 and c == 0:
    print("This equation has infinite solutions")
elif a == 0 or discriminant < 0:
    print("This equation has no solutions")
elif discriminant == 0:
    print("This equation has one solution: x =", -b/(2 *a))
elif discriminant > 0:
    print("This equation has two solutions: x =", (-b + discriminant)/(2 * a), "and x =", (-b - discriminant)/(2 * a))


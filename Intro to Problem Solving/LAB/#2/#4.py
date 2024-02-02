# Brian
# Lab 1: Area of a Triangle  
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


from math import sin, pi

base = float(input("Enter the Length of the triangle base: "))
side_a = float(input("Enter the length of the triangles side A: "))
angle_gamma = float(input("Enter the value of angle Gamma in degrees: "))

angle_gamma = (angle_gamma * pi)/180

print("The area of the triangle is", side_a * base * (sin(angle_gamma)/2))
# Brian
# HW 2: The BEE Calculator   
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

gender = input("Enter your gender (F for female, M for male): ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

if gender == 'F':
    Bee = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
else:
    Bee = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)

print("Your BEE is:", Bee)
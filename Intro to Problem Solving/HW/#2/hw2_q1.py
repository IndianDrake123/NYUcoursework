# Brian
# HW 1: Pizza Party, Let's Celebrate!
# Date Due: 9/22/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

from math import ceil

guests = int(input("Enter the number of guests: "))
slices_per_guest = int(input("Enter the number of pizza slices seach guest will eat: "))

total_slices_needed = guests * slices_per_guest

print("Minimum number of whole large pizzas required:", ceil(total_slices_needed/8))
print("Total number of large pizza slices needed:", total_slices_needed)
print("Number of large pizza slices left over:", 8 - (total_slices_needed%8))
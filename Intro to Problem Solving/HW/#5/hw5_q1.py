"""
Author: Brian Thomas 
Assignment / Part: HW5 - Q1 Halloween Candy Thief  
Date due: October 26, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

initials = input("Enter the initials of the suspects: ").replace(' ', '')
candy_wrappers = input("Enter the candy wrappers: ").replace(' ', '')
suspects = ''

initials_no_repeats = ''
candy_wrappres_no_repeats = ''
for initial in initials:
    if initial not in initials_no_repeats and initial.isalpha():
        initials_no_repeats += initial

for wrapper in candy_wrappers:
    if wrapper not in candy_wrappres_no_repeats and initial.isalpha():
        candy_wrappres_no_repeats += wrapper

for initial in initials_no_repeats:
    for candy in candy_wrappres_no_repeats:
        if initial == candy:
            suspects += initial
            
if len(suspects) > 0:
    for suspect in suspects:
        print(f"{suspect} is a candy thief suspect")
else:
    print("No candy thief found")




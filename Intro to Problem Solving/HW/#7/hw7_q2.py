"""
Author: Brian Thomas 
Assignment / Part: HW7 - Q2 Read Between The Words
Date due: November 9, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def get_word_count(file_path):        
    try:
        file = open(file_path, 'r')

    except FileNotFoundError:
        print(f"Warning: File '{file_path}' not found.")
        return 0
    
    word_tot = 0
    part_of_word = False

    for line in file:
        for char in line:
            if char.isalnum():
                if not part_of_word:
                    part_of_word = True
                    word_tot += 1
            else:
                part_of_word = False

    file.close()

    return word_tot 
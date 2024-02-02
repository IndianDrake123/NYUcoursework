"""
Author: Brian Thomas 
Assignment / Part: HW6 - Q2 Word Pyramid 
Date due: November 2, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def create_word_pyramid(char, levels):
    word_pyramid = ""
    for i in range(levels):
        word_pyramid += char * (i + 1) + '\n'
        char = chr(ord(char) + 1)

    return word_pyramid

def add_pyramid_level(old_pyramid):
    amt = 1
    for char in old_pyramid:
        if ord(char) == ord(old_pyramid[-2]):
            amt += 1

    char = chr(ord(old_pyramid[-2]) + 1)
    new_level = char * amt

    return old_pyramid + new_level + '\n'

def count_pyramid_levels(pyramid):
    levels = 0
    for char in pyramid:
        if char == '\n':
            levels += 1

    return levels

def main():
    char = 'B'
    levels = 5
    word_pyramid = create_word_pyramid(char, levels)
    print("Word Pyramid:")
    print(word_pyramid)
    updated_pyramid = add_pyramid_level(word_pyramid)
    print("\nUpdated Word Pyramid:")
    print(updated_pyramid)
    print("\nNumber of Levels in Pyramid:", count_pyramid_levels(updated_pyramid))

main()
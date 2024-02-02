"""
Author: Brian Thomas 
Assignment / Part: HW7 - Q1 Word Operations in a File with Functions
Date due: November 2, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def find_longest_word_in_file(file_path):
    try:
        file = open(file_path, 'r')

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0
    
    file_content = file.read()
    word = ""
    longest_word = ""

    for char in file_content:
        if char.isalnum() or char == "'":
            word += char
        else:
            if len(word) > len(longest_word):
                longest_word = word
            
            word = ""

    if len(word) > len(longest_word):
        longest_word = word
    
    file.close()
    return longest_word

def replace_word_in_file(file_path, target, replacement):
    try:
        file = open(file_path, 'r')
        
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0

    content = file.read()
    modified = ""
    word = ""

    for char in content:
        if char.isalnum() or char == "'":
            word += char
        else:
            if word == target:
                modified += replacement
            else:
                modified += word

            modified += char
            word = ""
 
            if word == target:
                modified += replacement
            else:
                modified += word

    with open(file_path, 'w') as file:
        file.write(modified)

    file.close()
        
def count_word_occurrences_in_file(file_path, target):
    try:
        file = open(file_path, 'r')

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0
    
    content = file.read()
    count = 0
    word = ""
    
    for char in content:
        if char.isalnum() or char == "'":
            word += char
        else:
            if word == target:
                count += 1

            word = ""
            
    if word == target:
        count += 1
    
    return count

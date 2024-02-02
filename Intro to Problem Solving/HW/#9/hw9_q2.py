"""
Author: Brian Thomas 
Assignment / Part: HW9 - Q2 Group Anagrams
Date due: November 30, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def group_anagrams(input_file):
    try:
        file = open(input_file, 'r')
    except FileNotFoundError:
        print("Error: Unable to read the file. Please check the file path.")
        return 

    content = file.readlines()
    words = [word.strip() for word in content]
    anagrams = []

    for word in words:
        anagram_set = []
        sorted_word = sorted(word)
        for check_word in words:
            sorted_check_word = sorted(check_word)
            if sorted_word == sorted_check_word:
                anagram_set.append(check_word)
        
        if anagram_set not in anagrams:
            anagrams.append(anagram_set)

    return anagrams

def main():
    directory = 'sample.txt'
    anagrams = group_anagrams(directory)
    print(anagrams)

main()
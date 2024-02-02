"""
Author: Brian Thomas 
Assignment / Part: HW9 - Q3 Word Frequency and Index Tracker
Date due: November 30, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def word_frequency_counter(input_file):
    try:
        file = open(input_file, 'r')
    except FileNotFoundError:
        print("Error: Unable to read the file. Please check the file path.")
        return
    
    content = file.readlines()
    sentences = [sentence.strip() for sentence in content]
    word_count = {}
    for sentence in sentences:
        sentence = sentence.split()
        for word in range(len(sentence)):
            if sentence[word] not in word_count:
                word_count[sentence[word]] = (1, [word])
            else:
                count, pos = word_count[sentence[word]]
                count += 1 
                pos.append(word)
                word_count[sentence[word]] = (count, pos)

    return word_count

def main():
    file_path = 'sample3.txt'
    word_frequencies = word_frequency_counter(file_path)
    print(word_frequencies)

main()
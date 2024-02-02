"""
Author: Brian Thomas 
Assignment / Part: HW8 - Q1 Nucleotidal Arithmetic
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def update_frequencies(old, new):
    updated_lst = []
    a = 0 
    c = 0
    t = 0
    g = 0

    for letter in new:
        if letter == 'A':
            a += 1
        elif letter == 'C':
            c += 1
        elif letter == 'T':
            t += 1
        elif letter == 'G':
            g += 1
    
    for tple in old:
        tple = list(tple)
        if tple[0] == 'A':
            updated_lst.append(('A', tple[1] + a))
        elif tple[0] == 'C':
            updated_lst.append(('C', tple[1] + c))
        elif tple[0] == 'T':
            updated_lst.append(('T', tple[1] + t))
        elif tple[0] == 'G':
            updated_lst.append(('G', tple[1] + g))

    print(f"Number of nucleotides added: A -> {a} | C -> {c} | T -> {t} | G -> {g}")
    return updated_lst

def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)

main()
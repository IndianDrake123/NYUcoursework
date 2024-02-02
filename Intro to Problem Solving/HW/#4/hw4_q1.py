"""
Author: Brian Thomas 
Assignment / Part: HW4 - Q1 Tamako Market 
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

mochiko = int(input("Enter an amount (g) of mochiko: "))//(220 * 3)
sugar = int(input("Enter an amount (g) of sugar: "))//(220 * 1.5)
cornstarch = int(input("Enter an amount (g) of cornstarch: "))//(220 * 2)
anko = int(input("Enter an amount (g) of anko: "))//220

batches = 0
if mochiko < sugar and mochiko < cornstarch and mochiko < anko:
    batches = mochiko
elif sugar < mochiko and sugar < cornstarch and sugar < anko:
    batches = sugar
elif cornstarch < sugar and cornstarch < mochiko and cornstarch < anko:
    batches = cornstarch
else:
    batches = anko

print(f"With this amount of ingredients, you can make {int(batches)} batch(es) or 24 mochi")


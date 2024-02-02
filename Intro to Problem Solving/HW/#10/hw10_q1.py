"""
Author: Brian Thomas 
Assignment / Part: HW10 - Q1 Tools Of The Trade
Date due: December 9, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import random

class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100:.1f} / 100 strength)"

    def does_break(self):
        if random.random() < .5 * self.strength: 
            return True
        else:
            return False

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    number_of_tests = 100
    number_of_breaks = 0

    for i in range(number_of_tests):
        if danelectro.does_break():
            number_of_breaks += 1

    percentage = (number_of_breaks / number_of_tests) * 100
    print(f"The {danelectro.model} broke {round(percentage)}% of the time in {number_of_tests} tests!")

main()

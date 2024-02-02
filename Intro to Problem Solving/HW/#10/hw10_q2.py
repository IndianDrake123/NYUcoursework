"""
Author: Brian Thomas 
Assignment / Part: HW10 - Q2 Artist of The Year
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
        random_value = random.random()
        return random_value < 0.5 * self.strength

class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def __str__(self):
        instrument_list = ", ".join(str(instrument) for instrument in self.instruments)
        return f"Musician object '{self.stage_name}', owning {instrument_list}"

    def pick_instrument(self, instrument_index=None):
        if len(self.instruments) == 0:
            return None
        
        if instrument_index is None:
            return random.choice(self.instruments)
        elif instrument_index >= len(self.instruments):
            last_instrument = self.instruments[len(self.instruments) - 1]
            return last_instrument
        else:
            return self.instruments[instrument_index]

danelectro = Instrument("Stock '59", "Danelectro", 0.25)
fender_vi = Instrument("VI Bass", "Fender", 0.99)
four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
gear = [danelectro, fender_vi, four_double_o_one]

sad_musician = Musician("Robert Smith", gear)

instrument1 = sad_musician.pick_instrument(2)
instrument2 = sad_musician.pick_instrument(100000000)
instrument3 = sad_musician.pick_instrument()

print(instrument1)
print(instrument2)
print(instrument3)

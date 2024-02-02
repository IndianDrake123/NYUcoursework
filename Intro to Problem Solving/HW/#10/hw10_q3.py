"""
Author: Brian Thomas 
Assignment / Part: HW10 - Q3 Battle of The Bands
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

def get_name_of_battle_winner(musician_a, musician_b):
    if len(musician_a.instruments) == 0 and len(musician_b.instruments) == 0:
        return "NO CONTEST"
    elif not musician_a.instruments:
        return musician_b.stage_name
    elif not musician_b.instruments:
        return musician_a.stage_name

    instrument_a = musician_a.pick_instrument()
    instrument_b = musician_b.pick_instrument()

    print(f"{musician_a.stage_name} picked a {instrument_a}!")
    print(f"{musician_b.stage_name} picked a {instrument_b}!")

    if instrument_a.strength > instrument_b.strength:
        if instrument_a.does_break():
            print(f'{musician_a.stage_name}\'s {instrument_a.model} broke!')
            return musician_b.stage_name
        else:
            return musician_a.stage_name
    elif instrument_b.strength > instrument_a.strength:
        if instrument_b.does_break():
            print(f'{musician_b.stage_name}\'s {instrument_b.model} broke!')
            return musician_a.stage_name
        else:
            return musician_b.stage_name
    else:
        random_winner = random.choice([musician_a.stage_name, musician_b.stage_name])
        print("Both musicians' instruments are the same strength. The winner will be decided by the whim of chance.")
        return random_winner

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    instruments = [danelectro, fender_vi, four_double_o_one]

    sad_musician = Musician("Robert Smith", instruments)
    less_sad_musician = Musician("Miki Berenyi", instruments)

    number_of_duels = 10
    for duel_number in range(1, number_of_duels + 1):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number} IS {winner_name}!", end="\n\n")

main()

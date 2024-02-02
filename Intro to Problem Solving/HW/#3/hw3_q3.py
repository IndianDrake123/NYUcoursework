"""
Author: Brian Thomas 
Assignment / Part: HW3 - Q3 2ne1
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

import random
play = input("Would you like to play 'Twenty-One'? [y/n] ")

while play != 'y' and play != 'n':
    play = input("Would you like to play 'Twenty-One'? [y/n] ")

if play == 'n':
    print("Thank you for playing!")
elif play == 'y':
    player_card_one = random.randint(1, 11)
    player_card_two = random.randint(1, 11)
    player_cards = player_card_one + player_card_two
    print("Your cards are worth", player_card_one, "and", player_card_two)

    new_card = input("Would you like another card? [y/n] ")

    while new_card != 'y' and new_card != 'n':
        new_card = input("Would you like to play 'Twenty-One'? [y/n] ")

    if new_card == 'y':
        player_cards += random.randint(1, 11)

    dealer = random.randint(0, 100)
    while dealer < 3 or dealer > 33:
        dealer = random.randint(0, 100)

    print("your score is", player_cards)
    print("Your opponent's scores is", dealer)

    if (player_cards > dealer and not player_cards > 21) or (dealer > 21 and not player_cards > 21):
        print("You won! Your score was", player_cards)
    elif player_cards == dealer or (player_cards > 21 and dealer > 21):
        print("It's a draw!")
    elif (dealer > player_cards and not dealer > 21) or player_cards > 21:
        print("Your opponent wins! Their score was", dealer)


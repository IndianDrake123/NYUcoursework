"""
Author: Brian Thomas 
Assignment / Part: HW4 - Q2 Must be funny in the rich man's world 
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

players = int(input("How many players played this round? "))
while players <= 0:
    print("invalid input. How many players played this round?")
    players = int(input("How many players played this round? "))

winning_player = ''
winning_amount = -1 
for player in range(players):
    player_total = 0
    player_totals = str()
    is_done = input("Enter the value of a property/asset, or DONE to finish: ")
    while is_done != 'DONE':
        player_total += float(is_done)
        is_done = input("Enter the value of a property/asset, or DONE to finish: ")

    if player_total > winning_amount:
        winning_amount = player_total
        winning_player = str(player + 1)
    elif player_total == winning_amount:
        winning_player += ' and ' + str(player + 1)
    print(f"player {player + 1} has {player_total} dollars")
            
if len(winning_player) < 8: 
    print(f'congratulations player {winning_player}! you won with ${winning_amount}!')
else:
    print(f'congratulations players {winning_player}! you all tied with ${winning_amount}!')


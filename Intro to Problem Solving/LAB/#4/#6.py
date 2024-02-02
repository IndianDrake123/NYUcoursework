import random 

print("Welcome to Blackjack!")
dealer = random.randint(2, 21)
player = random.randint(1, 11)
print("Your current card sum is:", player)
deal_or_stand = input("What would you like to do next?: (Deal, Stand) ")
while deal_or_stand != 's' and player < 21:
    player += random.randint(1, 11)
    print("Your current card sum is:", player)
    deal_or_stand = input("What would you like to do next?: (Deal, Stand) ")

if player < dealer or player > 21:
    print("You lost! Your card sum was", player, "and the dealer's was", dealer)
elif player == dealer:
    print("You tied! Your card sum was", player, "and the dealer's was", dealer)
else:
    print("You won! Your card sum was", player, "and the dealer's was", dealer)
print("Enter number of coins")
quarters = float(input("Number of quarters: ")) * .25
dimes = float(input("Number of dimes: ")) * .1
nickels = float(input("Number of nickels: ")) * .05
pennies = float(input("Number of pennies: ")) * .01

total_cents = quarters + dimes + nickels + pennies
dollars = int(total_cents // 1)
cents = round(total_cents % 1, 2)

print("The total is", dollars, "dollar(s) and", cents, "cent(s)")
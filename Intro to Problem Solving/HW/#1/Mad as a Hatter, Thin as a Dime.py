dollars = int((input("Enter amount of dollars: ")))
cents = int(input("Enter amounts of cents: "))

total_cents = cents 

quarters = int(total_cents//25)

total_cents -= quarters * 25 

dimes = int(total_cents//10)

total_cents -= dimes * 10 

nickels = int(total_cents//5)

total_cents -= nickels * 5 

pennies = int(total_cents//1)

total_cents -= pennies * 1 

quarters += int(dollars/.25)

print(dollars, "dollars and", cents, "cents are:", quarters, "quarters,", dimes, "dimes,", nickels, "nickels and,", pennies, "pennies")
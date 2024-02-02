num_of_factorials = int(input("How many factorials would you like to do? "))
while num_of_factorials <= 0:
    print("ERROR: Please enter a positive integer. ")
    num_of_factorials = int(input("How many factorials would you like to do? "))

for i in range(num_of_factorials):
    factorial = 1
    num = int(input("Please enter a positive integer: "))
    if num == 0:
        print(f"0! is equal to {factorial}")
    else:
        for i2 in range(num, 1, -1):               
            factorial *= i2  
            num -= 1

        print(factorial)

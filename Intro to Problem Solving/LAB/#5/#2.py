cont = input("play? (enter/q)")
while cont != 'q':
    first_factor = int(input("Please input your first factor: "))
    second_factor = int(input("Please input your second factor: "))
    product = 0
    if first_factor <= 0 or second_factor <= 0:
        print("ERROR: Positive integers must be entered!")
        cont = input("play? (enter/q)")
    else:
        for i in range(second_factor):
            product += first_factor

        print(product)
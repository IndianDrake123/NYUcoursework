width = int(input("Python needs to tell you a secret. How many characters wide can is message be? "))
each_row = ''
for col in range(0, width):
    each_row = ''
    for row in range(0, width):
        if col == row or width - row - 1 == col:
            each_row += "X"
        else:
            each_row += " "

    print(each_row)

for row in range(0, width):
    each_row = ''
    for col in range(0, width):
        if (row == 0 or row == width - 1):
            if col == 0 or col == width - 1:
                each_row += " "
            else:
                each_row += 'O'
        elif (col == 0 or col == width - 1):
            each_row += 'O'
        else:
            each_row += " "
    
    print(each_row)

for col in range(0, width):
    each_row = ''
    for row in range(0, width):
        if col == row or width - row - 1 == col:
            each_row += "X"
        else:
            each_row += " "

    print(each_row)
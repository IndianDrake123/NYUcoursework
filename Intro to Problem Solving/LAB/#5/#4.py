import random
for row in range(1, 11):
    reverse = random.random()
    each_row =''
    if reverse > .5:
        for col in range(1, row + 1):
            each_row += str(row * col) + '  '
    else:
        for col in range(row, 0, -1):
            each_row += str(row * col) + '  '
    print(each_row)
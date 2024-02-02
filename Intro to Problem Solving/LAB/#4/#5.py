num_values = int(input("Please enter how many postiive values you want to consider: "))
num1 = 0
largest = 0
if num_values > 0:
    for i in range(num_values):
        num2 = float(input(""))
        if num2 > num1:
            largest = num2
    print("The largest of these values is", largest)
else:
    print("There are no values to check")

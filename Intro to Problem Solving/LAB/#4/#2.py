# Brian
# Lab 3: Single use calculator   
# Date Due: 9/29/23
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


play = input("Hit enter to continue and Q to quit calculator: ")
while play != 'Q':
    first_num = float(input("first: "))
    operation = input("operation (+, -, *, /): ")
    second_num = float(input("second: "))

    if operation == "+":
        print(first_num, "+", second_num, '=', first_num + second_num)
    elif operation == "-":
        print(first_num, "-", second_num, '=', first_num - second_num)
    elif operation == "*":
        print(first_num, "*", second_num, '=', first_num * second_num)
    elif operation == "/":
        if second_num != 0:
            print(first_num, "/", second_num, '=', first_num/second_num)
        else:
            print(first_num, "/", second_num, 'is an invalid operation')
    else:
        print(first_num, operation, second_num, 'is an invalid operation')
    
    play = input("Hit enter to continue and Q to quit calculator: ")

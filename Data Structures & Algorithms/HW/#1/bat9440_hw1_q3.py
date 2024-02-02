#a 

def sum_of_squares_of_nums_smaller_than_n(n):
    sum = 0
    for i in range(1, n):
        sum += i ** 2

    return sum

print(sum_of_squares_of_nums_smaller_than_n(5))

#b

def sum_of_squares_of_nums_smaller_than_n(n):
    return sum(i**2 for i in range(n))


print(sum_of_squares_of_nums_smaller_than_n(5))

#c

def sum_of_odd_squares(n):
    sum = 0
    for i in range(1, n):
        if i % 2 == 1:
            sum += i ** 2

    return sum

print(sum_of_odd_squares(5))

#d

def sum_of_odd_squares(n):
    return sum(i**2 for i in range(n) if i % 2 == 1)

print(sum_of_odd_squares(5))


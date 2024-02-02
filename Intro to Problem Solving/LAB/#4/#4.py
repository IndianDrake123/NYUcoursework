base = float(input("Please enter a positive integer to serve as the base: "))
power = float(input("Please enter a positive integer to serve as the highest power: "))

if base < 0 or power < 0 or base % 1 != 0 or power % 1 != 0:
    print("ERROR: Both values must be POSITIVE INTEGERS")
else:
    for i in range(int(power) + 1):
        print(base, '^', i, '=', base ** i)

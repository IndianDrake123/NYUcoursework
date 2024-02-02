init_num = int(input("num less than 100: "))

num = init_num

roman_numerals = "L" * (num // 50)
num %= 50

roman_numerals += "X" * (num//10)
num %= 10

roman_numerals += "V" * (num//5)
num %= 5

roman_numerals += "I" * (num//1)
num %= 1

print(init_num, "is", roman_numerals, "in roman numerals")
"""string = input("Enter a string to be printed (in the format [text]-[text]...): ")

string = string.split('-')
print("printing")
for part in string:
    print(part)"""

string = input("Enter a string to be printed (in the format [text]-[text]...): ")
for wrd in string:
    if wrd == '-':
        print()
    else:
        print(wrd, end='')
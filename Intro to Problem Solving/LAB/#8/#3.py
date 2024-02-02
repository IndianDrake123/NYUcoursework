def decode_roman_file(romanfile, outFile):
    with open(romanfile, 'r') as file1:
        msg = decode_entire_msg(file1)

    with open(outFile, 'w') as file2:
        file2.write(msg)

def decode_entire_msg(roman_file):
    with open(roman_file, 'r') as file:
        msg = str()
        skip = 0 
        skipped = 0
        full = [line for line in file]
        print(full)
        for line in full:
            for char in line:
                if char != '\n':
                    if char.isdigit():
                        skip = char
                    if skip != 0:
                        if skipped != skip:
                            skipped += 1
                            print(skipped)
                        elif skip == skipped:
                            print('r')
                            skipped = 0
                            msg += char

    print(msg)

def main():
    ROMAN_FILE = 'roman_code_msg.txt'
    ROMAN_DECODED_FILE = 'secret_msg.txt'

    #decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE)

    decode_entire_msg(str(ROMAN_FILE))

main()
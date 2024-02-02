phrase = input('Please enter your message:\n')
#Originally, the Green goBlin Rested in HiS forest for maNY Eras
start_pos = 0
end_pos = phrase.find(' ')
msg = ''

while end_pos < len(phrase) and end_pos != -1:
    phrase_part = phrase[start_pos:end_pos]
    first_char = phrase_part[0]
    if first_char.isupper():
        msg += phrase_part[0]
        for char in phrase_part[1:]:
            if char.isupper():
                msg = msg.replace(first_char, '')

    start_pos = end_pos + 1
    end_pos = phrase.find(' ', start_pos)

last_wrd = phrase[start_pos:]
first_char = last_wrd[0]
if first_char.isupper():
    msg += last_wrd[0]
    for char in last_wrd[1:]:
        if char.isupper():
            msg = msg.replace(first_char, '')

print(msg)
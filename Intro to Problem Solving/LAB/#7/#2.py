import time

phrase = input('Enter a phrase: ')
start_pos = 0
end_pos = phrase.find(' ')

while end_pos < len(phrase) and end_pos != -1:
    phrase_part = phrase[start_pos:end_pos]
    if phrase_part.isdigit():
        phrase = phrase.replace(phrase_part, 'x' * len(phrase_part), 1)

    start_pos = end_pos + 1
    end_pos = phrase.find(' ', start_pos)

print(phrase)
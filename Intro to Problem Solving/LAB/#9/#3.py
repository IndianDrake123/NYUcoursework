import random 

def get_random_word(file_path):
    try:
        file = open(file_path)
    
    except FileNotFoundError:
        print("Warning. File not found!")
        return 0
    
    words = []
    content = file.readlines()
    for line in content:
        line = line.strip()
        line = line.split()
        for word in line:
            words.append(word)

    random_word = random.choice(words)
    file.close()
    return random_word

def main():
    print(get_random_word("words.txt"))

main()
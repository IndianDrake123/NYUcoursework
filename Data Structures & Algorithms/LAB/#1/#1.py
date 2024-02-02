def can_construct(word, letters):
    all_letters = []
    for letter in letters:
        all_letters.append(letter)

    reconstruct = ''
    for letter in word:
        if letter in all_letters:
            all_letters.remove(letter)
            reconstruct += letter

    if reconstruct == word:
        return True
    else:
        return False
        
    
#print(can_construct("apples", "aplepls"))

class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.num = f'{a} {'-' if b < 0 else '+'} {abs(b)}i'
    
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)
    
    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        new_complex = Complex(a, b)
    
    def __mul__(self, other):
        num = (self.a * other.a) - (self.b * other.b)
        i_val = (self.a * other.b) + (self.b * other.a)
        new_complex = Complex(num, i_val)
    
    def __repr__(self) -> str:
        return f'{self.a} {'-' if self.b < 0 else '+'} {abs(self.b)}i'

    def __iadd__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        self.num =  f'{self.a} {'-' if self.b < 0 else '+'} {abs(self.b)}i'
        return self

cplx1 = Complex(5, 2)
cplx2 = Complex(3, 3)
#print(cplx1 + cplx2)
#print(cplx1 - cplx2)
#print(cplx1 * cplx2)

from random import randint

def create_function(n):
    rand_ord = []
    ran = n - 1
    while len(rand_ord) != n:
        random = randint(0, ran)
        if random not in rand_ord:
            rand_ord.append(random)

    return rand_ord

#print(create_function(6))

def scramble_word(word):
    scrambled = ''
    order = create_function(len(word))
    for ord in order:
        scrambled += word[ord]

    return ' '.join(scrambled)

#print(scramble_word("pokemon"))
word = 'pokemon'
print('unscramble the word:', scramble_word(word))
try_num = 1
inp = input(f'Try #{try_num}: ')
while inp != word:
    print('Wrong!')
    try_num += 1
    inp = input(f'Try #{try_num}: ')

print('Yay, you got it!')
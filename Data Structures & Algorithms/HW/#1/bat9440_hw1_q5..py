def fibs(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for curr in fibs(8):
    print(curr)

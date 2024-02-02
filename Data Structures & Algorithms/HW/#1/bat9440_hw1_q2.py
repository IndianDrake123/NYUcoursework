#part A

def shift(lst, k):
    length = len(lst)
    lst[:] = lst[k:length] + lst[0:k]

lst = [1, 2, 3, 4, 5, 6]

shift(lst, 2)
print(lst)

#part B

def shift(lst, k, direction='left'):
    length = len(lst)
    if direction == 'left':
        lst[:] = lst[k:length] + lst[0:k]
    if direction == 'right':
        lst[:] = lst[length - k:length] + lst[0:length - k]

lst1 = [1, 2, 3, 4, 5, 6]
shift(lst1, 2)
print(lst1)
lst2 = [1, 2, 3, 4, 5, 6]
shift(lst2, 2, 'right')
print(lst2)
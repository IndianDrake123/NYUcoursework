import random

def shuffle_create(lst):
    n = len(lst)
    new_lst = []
    for i in range(n - 1, 0, -1):
        j = i if i == 0 else random.randint(0, i)    
        new_lst.append(lst[j])

    return new_lst

def shuffle_in_place(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        j = i if i == 0 else random.randint(0, i)    
        lst[i], lst[j] = lst[j], lst[i]

    return lst

def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy",
"Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))
# First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))
    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))
# Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))

main()

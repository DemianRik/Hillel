list_1 = [0, 1, 2, 0, 3, 0, 4]
print(list_1)

def move_zeros_to_end(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

result = move_zeros_to_end(list_1)
print(result)

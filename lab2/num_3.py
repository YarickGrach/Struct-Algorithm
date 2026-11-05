def recursive_reverse(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + recursive_reverse(lst[1:-1]) + [lst[0]]

print(recursive_reverse([1, 2, 3, 4, 5]))

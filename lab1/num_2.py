a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
print("Array: ", *a)

def alg_1(arr):               #O(n)
    mx = arr[len(arr) - 1]
    mn = arr[len(arr) - 1]

    for i in arr:
        mx = i if i > mx else mx
        mn = i if i < mn else mn

    return (mx, mn)

def alg_2(arr):
    mx, mn = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    i = 2
    n = len(arr)

    while i + 1 < n:
        small, big = (arr[i], arr[i + 1]) if arr[i] < arr[i + 1] else (arr[i + 1], arr[i])
        if small < mn:
            mn = small
        if big > mx:
            mx = big
        i += 2

    if i < n:
        if arr[i] < mn:
            mn = arr[i]
        elif arr[i] > mx:
            mx = arr[i]

    return (mx, mn)

mx, mn = alg_1(a)
print(f"\nAlg_1:\nMax = {mx}\nMin = {mn}\n")

mx, mn = alg_2(a)
print(f"Alg_2:\nMax = {mx}\nMin = {mn}")

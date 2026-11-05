def tribonacci(n):
    if n < 3:
        return (0, 0, 1)[n]     #Базовый случай
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)    #Рекурсивный случай

print([tribonacci(i) for i in range(10)])

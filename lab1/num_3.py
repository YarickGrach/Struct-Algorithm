a = 1
b = -5
c = -50

def sqr_eq(a, b, c):
    D = b ** 2 - 4 * a * c
    x1, x2 = ((-b + D ** 0.5) / 2 / a), ((-b - D ** 0.5) / 2 / a)
    answer = x1 if x1 >= 0 else x2
    return answer

print(sqr_eq(a, b, c))

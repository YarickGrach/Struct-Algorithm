import time
import matplotlib.pyplot as plt
from functools import lru_cache

def base(n, arr):
    if n < 2:
        return arr[n]
    return base(n - 1, arr) + base(n - 2, arr)

def fibonacci(n):
    return base(n, (0, 1))

def lucas(n):
    return base(n, (2, 1))

def fib_with_lucas(n):
    i = n // 2
    j = n - i
    return ((fibonacci(i) * lucas(j) + fibonacci(j) * lucas(i)) // 2)

def lucas_with_fib(n):
    return (fibonacci(n - 1) + fibonacci(n + 1))

print(fibonacci(5), fib_with_lucas(5), lucas_with_fib(5), lucas(5), sep="\n")

def measure(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start

Ns = list(range(20, 33))

times_fib = [measure(fibonacci, n) for n in Ns]
times_fib_lucas = [measure(fib_with_lucas, n) for n in Ns]

plt.figure(figsize=(9, 5))
plt.plot(Ns, times_fib, 'o-', label='fibonacci(n)')
plt.plot(Ns, times_fib_lucas, 's-', label='fib_with_lucas(n)')
plt.xlabel('n')
plt.ylabel('время, с')
plt.yscale('log')
plt.title('Сравнение fibonacci() и fib_with_lucas()')
plt.grid(True, which='both', ls=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('fib_comparison.png', dpi=150)
plt.show()

# Проверка корректности
for n in range(15):
    assert fibonacci(n) == fib_with_lucas(n), f"n={n}: {fibonacci(n)} != {fib_with_lucas(n)}"
    assert lucas(n) == lucas_with_fib(n) if n > 0 else True
print("Все проверки пройдены")

import timeit, random, matplotlib.pyplot as plt

def bench_in_set(n, repeats=5, present=True):
    s = set(range(n))
    def op():
        k = random.randrange(n) if present else n + 1   # заведомо отсутствующий
        return k in s
    return min(timeit.repeat(op, number=1000, repeat=repeats)) / 1000

def bench_in_list(n, repeats=5, present=True):
    lst = list(range(n))
    def op():
        k = random.randrange(n) if present else n + 1
        return k in lst
    return min(timeit.repeat(op, number=1000, repeat=repeats)) / 1000

sizes = [10**2, 5*10**2, 10**3, 5*10**3, 10**4, 5*10**4, 10**5]

t_set_p  = [bench_in_set(n,  present=True)  for n in sizes]
t_set_a  = [bench_in_set(n,  present=False) for n in sizes]
t_list_p = [bench_in_list(n, present=True)  for n in sizes]
t_list_a = [bench_in_list(n, present=False) for n in sizes]

plt.figure(figsize=(9, 5))
plt.plot(sizes, t_set_p,  'o-', label='set: x in s (есть)')
plt.plot(sizes, t_set_a,  'o--', label='set: x in s (нет)')
plt.plot(sizes, t_list_p, 's-', label='list: x in lst (есть)')
plt.plot(sizes, t_list_a, 's--', label='list: x in lst (нет)')
plt.xscale('log'); plt.yscale('log')
plt.xlabel('n (размер контейнера)'); plt.ylabel('время одной операции, с')
plt.title('Задание 5: in — множество vs список')
plt.grid(True, which='both', ls=':', alpha=0.6)
plt.legend(); plt.tight_layout(); plt.savefig('task5_in.png', dpi=150)
plt.show()

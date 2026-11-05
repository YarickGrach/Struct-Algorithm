import timeit, random, matplotlib.pyplot as plt

def bench_del_dict(n, repeats=5):
    d = {i: i for i in range(n)}
    keys = list(d.keys())
    def op():
        k = keys[random.randrange(n)]
        del d[k]
        d[k] = k          # возвращаем обратно, чтобы размер не менялся
    return min(timeit.repeat(op, number=1000, repeat=repeats)) / 1000

def bench_del_list_mid(n, repeats=5):
    lst = list(range(n))
    def op():
        i = random.randrange(n)
        x = lst.pop(i)
        lst.insert(i, x)
    return min(timeit.repeat(op, number=1000, repeat=repeats)) / 1000

def bench_del_list_front(n, repeats=5):
    lst = list(range(n))
    def op():
        x = lst.pop(0)
        lst.insert(0, x)
    return min(timeit.repeat(op, number=1000, repeat=repeats)) / 1000

sizes = [10**3, 5*10**3, 10**4, 5*10**4, 10**5, 5*10**5, 10**6]

t_dict  = [bench_del_dict(n)          for n in sizes]
t_mid   = [bench_del_list_mid(n)      for n in sizes]
t_front = [bench_del_list_front(n)    for n in sizes]

plt.figure(figsize=(9, 5))
plt.plot(sizes, t_dict,  'o-', label='dict: del d[k]')
plt.plot(sizes, t_mid,   's-', label='list: del lst[random]')
plt.plot(sizes, t_front, '^-', label='list: del lst[0] (худший)')
plt.xscale('log'); plt.yscale('log')
plt.xlabel('n (размер контейнера)'); plt.ylabel('время одной операции, с')
plt.title('Задание 4: del — словарь vs список')
plt.grid(True, which='both', ls=':', alpha=0.6)
plt.legend(); plt.tight_layout(); plt.savefig('task4_del.png', dpi=150)
plt.show()

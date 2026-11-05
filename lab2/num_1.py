import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)


def selection_sort(arr):
    """Сортировка выбором. O(n^2) во всех случаях."""
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quick_sort(arr):
    """Быстрая сортировка (in-place, схема Хоара, медиана из трёх)."""
    a = arr.copy()
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(a, lo, hi):
    if lo >= hi:
        return
    # медиана из трёх как опорный элемент (защита от худшего случая)
    mid = (lo + hi) // 2
    if a[lo] > a[mid]:
        a[lo], a[mid] = a[mid], a[lo]
    if a[lo] > a[hi]:
        a[lo], a[hi] = a[hi], a[lo]
    if a[mid] > a[hi]:
        a[mid], a[hi] = a[hi], a[mid]
    pivot = a[mid]

    i, j = lo, hi
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    _quick_sort(a, lo, j)
    _quick_sort(a, i, hi)

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


def run_experiment(sizes, repeats=3):
    """Возвращает три словаря с временами для трёх типов данных."""
    results = {
        "random":     {"selection": [], "quick": []},
        "sorted":     {"selection": [], "quick": []},
        "reversed":   {"selection": [], "quick": []},
    }

    for n in sizes:
        # 1. случайные
        random_data = [random.randint(0, 10 * n) for _ in range(n)]
        # 2. отсортированные
        sorted_data = list(range(n))
        # 3. обратно отсортированные
        reversed_data = list(range(n, 0, -1))

        for key, data in [("random", random_data),
                          ("sorted", sorted_data),
                          ("reversed", reversed_data)]:
            # берём минимум из нескольких запусков (устойчивее к шуму)
            t_sel = min(measure_time(selection_sort, data) for _ in range(repeats))
            t_qs  = min(measure_time(quick_sort,    data) for _ in range(repeats))
            results[key]["selection"].append(t_sel)
            results[key]["quick"].append(t_qs)

    return results


if __name__ == "__main__":
    # размеры подобраны так, чтобы сортировка выбором не выполнялась слишком долго
    sizes = [100, 200, 400, 600, 800, 1000, 1500, 2000, 3000, 4000]

    print("Запуск экспериментов...")
    results = run_experiment(sizes, repeats=3)

    # ---------- Построение графиков ----------
    titles = {
        "random":   "Случайные числа",
        "sorted":   "Отсортированный список",
        "reversed": "Отсортированный в обратную сторону",
    }

    for key in ["random", "sorted", "reversed"]:
        plt.figure(figsize=(9, 6))
        plt.plot(sizes, results[key]["selection"], 'o-',
                 label="Сортировка выбором", color="crimson")
        plt.plot(sizes, results[key]["quick"], 's-',
                 label="Быстрая сортировка", color="steelblue")
        plt.xlabel("Размер массива (n)")
        plt.ylabel("Время выполнения (сек)")
        plt.title(f"Зависимость времени сортировки от размера\n{ titles[key] }")
        plt.grid(True, alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"plot_{key}.png", dpi=130)
        plt.show()

    # ---------- Числовая таблица ----------
    print("\nРезультаты (время в секундах):")
    header = f"{'n':>6} | {'Случ. выбор':>12} {'Случ. quick':>12} | " \
             f"{'Сорт. выбор':>12} {'Сорт. quick':>12} | " \
             f"{'Обр. выбор':>12} {'Обр. quick':>12}"
    print(header)
    print("-" * len(header))
    for i, n in enumerate(sizes):
        print(f"{n:>6} | "
              f"{results['random']['selection'][i]:>12.5f} "
              f"{results['random']['quick'][i]:>12.5f} | "
              f"{results['sorted']['selection'][i]:>12.5f} "
              f"{results['sorted']['quick'][i]:>12.5f} | "
              f"{results['reversed']['selection'][i]:>12.5f} "
              f"{results['reversed']['quick'][i]:>12.5f}")

import statistics

def ar():
    arr = list(map(int, input().split()))
    print(arr)
    kol = len(arr)
    sred = sum(arr) / len(arr)
    minimum = min(arr)
    maximum = max(arr)
    print("Число элементов списка:", kol)
    print("Среднее значение списка:", sred)
    print("Минимальное значение списка:", minimum)
    print("Максимальное значение списка:", maximum)

ar()
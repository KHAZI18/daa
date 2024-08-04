import time
import matplotlib.pyplot as plt
from random import randint

def divide(a, low, high):
    if low < high:
        j = part(a, low, high)
        divide(a, low, j - 1)
        divide(a, j + 1, high)

def part(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high

    while True:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[low], a[j] = a[j], a[low]
    return j

def main():
    x = []
    y = []
    for n in range(10, 101, 10):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1, n))
        start = time.time()
        divide(a, 0, len(a) - 1)
        end = time.time()
        elapse = end - start
        y.append(elapse)
        print(a)
    plt.plot(x, y)
    plt.xlabel("input size")
    plt.ylabel("time")
    plt.show()

main()

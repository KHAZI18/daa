import time
import matplotlib.pyplot as plt
from random import randint

def bubblesort(a, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def main():
    x = []
    y = []
    for n in range(10,101,10):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))
        start = time.time()
        bubblesort(a,n)
        end = time.time()
        lapse = end-start
        y.append(lapse)
        print(a)
    plt.plot(x,y,label="selection sort")
    plt.xlabel("input")
    plt.ylabel("time")
    plt.show()
main()
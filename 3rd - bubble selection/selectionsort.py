import matplotlib.pyplot as plt
import time
from random import randint

def Selectionsort(a,n):
    for i in range (n-1):
        min=i
        for j in range (i+1,n):
            if(a[j]<a[min]):
                min=j

        a[i],a[min]=a[min],a[i]

def main():
    x=[]
    y=[]
    for n in range(10,101,10):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))
        print(a)
        start=time.time()
        Selectionsort(a,n)
        end=time.time()
        print(a)
        gaptime=end-start    
        y.append(gaptime)
    plt.bar(x,y)
    plt.xlabel("n size")
    plt.ylabel("time")
    plt.show()
main()
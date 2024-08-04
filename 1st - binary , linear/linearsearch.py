# import time
import random

def linear_search(arr, target):
    comp = 0
    for i in range(len(arr)):
        comp += 1
        if arr[i] == target:
            print("Element found at index", i)
            print(comp)
            return i
    print("element not found")
    return -1

def main():
    array_size = 1000
    arr = [random.randint(1, 100) for _ in range(array_size)]
    target = random.randint(1, 100)
    linear_search(arr, target)

if __name__ == "__main__":
    main()
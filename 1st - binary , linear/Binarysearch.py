camp = 0

def binary_search(lst, low, high, key):
    global camp
    if low > high:
        print("Key not found")
        return

    mid = (low + high) // 2
    if lst[mid] == key:
        print(f"Key found at position = {mid}")
    elif lst[mid] > key:
        binary_search(lst, low, mid - 1, key)
    else:
        binary_search(lst, mid + 1, high, key)
    camp += 1

def main():
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    key = 70
    binary_search(lst, 0, len(lst) - 1, key)
    print(f"Number of comparisons = {camp}")

if __name__ == "__main__":
    main() 
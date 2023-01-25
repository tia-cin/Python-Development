import random
import time

# scan each item in list asking if is equal to target 
def default_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

# 
def binary_search(values, target, lowest=None, highest=None):
    if lowest is None:
        lowest = 0
    if highest is None:
        highest = len(values) - 1

    if highest < lowest:
        return -1

    midval = (lowest + highest) // 2

    if values[midval] < target:
        return binary_search(values, target, midval+1, highest)
    elif target < values[midval]:
        return binary_search(values, target, lowest, midval-1)
    else:
        return midval

if __name__ == '__main__':
    length = 1000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        default_search(sorted_list, target)
    end = time.time()
    print(f"Default search: {(end - start) / length}s")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f"Binary search: {(end - start) / length}s")
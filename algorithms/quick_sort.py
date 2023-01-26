import time

def partition(vals, left, right):
    # set indexes & pivot (random value in the vals)
    l, r = left, right
    pivot = vals[right]

    # as long as left index is lower than right one
    while l < r:
        # when left ind is lower and left indexed val is less than pivot
        while l < right and vals[l] < pivot:
            l += 1 # update left index
        # when right ind is bigger and right indexed val is bigger or equal to pivot
        while r > left and vals[r] >= pivot:
            r -= 1 # update right index

        # switch if left index is lower
        if l < r:
            vals[l], vals[r] = vals[r], vals[l]
        print(vals)
    
    # switch if left indexed val is bigger than pivot
    if vals[l] > pivot:
        vals[l], vals[right] = vals[right], vals[l]

    return l


def quick_sort(vals, left, right):
    start = time.time()

    # left (first index)
    # right (last index)
    if left < right:
        partition_position = partition(vals, left, right)

        # recursion
        quick_sort(vals, left, partition_position - 1)
        quick_sort(vals, partition_position + 1, right)


    end = time.time()
    print(f"Time: {end - start}")


ex = [1,5,8,2,4,3,7,6,9]

print(quick_sort(ex, 0, len(ex) -1))

"""
    Time: 0.009135007858276367

    [1, 5, 8, 2, 4, 3, 7, 6, 9]
    [1, 5, 3, 2, 4, 8, 7, 6, 9]
    [1, 5, 3, 2, 4, 8, 7, 6, 9]
    [1, 2, 3, 5, 4, 6, 7, 8, 9]
    [1, 2, 3, 5, 4, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
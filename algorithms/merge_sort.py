import time

def merge_sort(vals):
    start = time.time()
    
    if len(vals) > 1:
        left = vals[:len(vals) // 2]
        right = vals[len(vals) // 2:]

        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                vals[k] = left[l]
                l += 1
            else:
                vals[k] = right[r]
                r += 1
            k += 1
        
        while l < len(left):
            vals[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            vals[k] = right[r]
            r += 1
            k += 1

        print(vals)


    end = time.time()
    print(f"Time: {end - start}")


ex = [1,5,8,2,4,3,7,6,9]

print(merge_sort(ex))

"""
    Time: 0.20833516120910645

    [1, 5]
    [2, 8]
    [1, 2, 5, 8]
    [3, 4]
    [6, 9]
    [6, 7, 9]
    [3, 4, 6, 7, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
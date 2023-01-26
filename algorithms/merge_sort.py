import time

def merge_sort(vals):
    start = time.time()
    
    # at least two items
    if len(vals) > 1:
        # split arr in halft
        left = vals[:len(vals) // 2]
        right = vals[len(vals) // 2:]

        # recursion
        merge_sort(left)
        merge_sort(right)

        # set indexes
        l, r = 0, 0 # left_index, right_index
        k = 0

        # as long as both indexes are lower than their arrs
        while l < len(left) and r < len(right):
            # when curr left val is lower than right curr val
            if left[l] < right[r]:
                vals[k] = left[l] # update original arr
                l += 1 # move to next
            else: # if right one was lower
                vals[k] = right[r]
                r += 1
            k += 1 # update original curr index

        # as log as left index is lower than its arr        
        while l < len(left):
            # curr original val is left curr val
            vals[k] = left[l]
            # update indexes
            l += 1
            k += 1

        # same with right arr and index
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
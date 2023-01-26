import time

def insertion_sort(vals):
    start = time.time()
    # start from position 1
    for i in range(1, len(vals)):
        # copy i current val
        j = i
        # as long as prev val is bigger than current and j is bigger than 0
        while vals[j - 1] > vals[j] and j > 0:
            # set prev as current & current to prev
            vals[j - 1], vals[j] = vals[j], vals[j - 1]
            # update j val to minus one
            j -= 1
    
            print(vals)
    end = time.time()
    print(f"Time: {end - start}")

ex = [1,5,8,2,4,3,7,6,9]

print(insertion_sort(ex))

# process graphic

""" 
    Time: 0.004053354263305664
    
    [1, 5, 2, 8, 4, 3, 7, 6, 9]
    [1, 2, 5, 8, 4, 3, 7, 6, 9]
    [1, 2, 5, 4, 8, 3, 7, 6, 9]
    [1, 2, 4, 5, 8, 3, 7, 6, 9]
    [1, 2, 4, 5, 3, 8, 7, 6, 9]
    [1, 2, 4, 3, 5, 8, 7, 6, 9]
    [1, 2, 3, 4, 5, 8, 7, 6, 9]
    [1, 2, 3, 4, 5, 7, 8, 6, 9]
    [1, 2, 3, 4, 5, 7, 6, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9] 

"""
import time

def selection_sort(vals):
    start = time.time()
    # ommit last one
    for i in range(0, len(vals) - 1):
        # assume curr index is where min value is located
        curr_min_i = i

        # scan all values after next from curr val
        for j in range(i + 1, len(vals)):
            # update curr_min_i when next val is smaller
            if vals[j] < vals[curr_min_i]:
                curr_min_i = j

        # switch positions
        vals[i], vals[curr_min_i] = vals[curr_min_i], vals[i]
        print(vals)
    end = time.time()
    print(f"Time: {end - start}")


ex = [1,5,8,2,4,3,7,6,9]

print(selection_sort(ex))

"""
    Time: 0.0036628246307373047

"""
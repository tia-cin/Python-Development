import time

def selection_sort(vals):
    start = time.time()
    for i in range(0, len(vals) - 1):
        curr_min_i = i

        for j in range(i + 1, len(vals)):
            if vals[j] < vals[curr_min_i]:
                curr_min_i = j

        vals[i], vals[curr_min_i] = vals[curr_min_i], vals[i]
        print(vals)
    end = time.time()
    print(f"Time: {end - start}")


ex = [1,5,8,2,4,3,7,6,9]

print(selection_sort(ex))
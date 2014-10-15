# Don't care about indices, nor the slice...just the sum.
def golden_max_slice(A): 
    max_ending = max_slice = 0 
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

print golden_max_slice([0, 2, 3, 2, -5, -3, 1])
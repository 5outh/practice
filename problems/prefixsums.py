"""
Get the sums of the prefixes of the list
"""
def prefix_sums(arr):
    sums = [0] * (len(arr) + 1)
    for i in xrange(1, len(sums)):
        sums[i] = sums[i-1] + arr[i-1]
    return sums

"""
Get the sums of the suffixes of a list
"""
def suffix_sums(arr):
    sums = [0] * (len(arr) + 1)
    for i in xrange(1, len(sums)):
        sums[i] = sums[i-1] + arr[-i]
    return sums

"""
Get the sum of elements in a slice from i to j
pres: prefix sums of array
"""
def sum_slice(pres, i, j):
    print pres[j], pres[i]
    return pres[j+1] - pres[i]

"""
Maximal number of "things" to pick up in m moves from a position k
"""
def mushroom(arr, k, m):
    mx = 0
    pres = prefix_sums(arr)
    for p in xrange(m):
        # bounds unchecked
        sm = sum_slice(pres, k-p, k + m - (2*p))
        mx = max(sm, mx)
    for p in xrange(m):
        # bounds unchecked
        sm = sum_slice(pres, (k-m) + (2*p), k+p)
        mx = max(sm, mx)
    return mx

arr = [2, 3, 4, 5]

print arr[-len(arr)]

print prefix_sums(arr)
print suffix_sums(arr)
print sum_slice(arr, 1, 2)
"""
Given an array of integers from 0 to m, return the counts array
"""
def count(A, m):
    arr = [0] * (m + 1)
    for i in A:
        arr[i] += 1
    return arr

"""
Count using a dictionary
"""
def count_dict(A):
    d = dict()
    for a in A:
        if d.get(a) is None:
            d[a] = 1
        else:
            d[a] += 1
    return d

"""
Check if it is possible to swap a single a in A for a 
single b in B to make sum(A) == sum(B)
"""
def find_swap(A, B):
    n = len(A)
    sumA = sum(A)
    sumB = sum(B)
    diff = sumB - sumA
    if(diff % 2 != 0):
        return False
    diff //= 2
    countDict = count_dict(A)
    for i in xrange(n):
        if (countDict.get(B[i] - diff) is not None):
            return True
    return False

swappableA = [4, 8, 4]
swappableB = [10, 2, 0]

print find_swap(swappableA, swappableB) # true
print count_dict(swappableA)
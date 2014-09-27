def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def partition(a, p, q):
    pivot = a[q]
    i = p-1
    for j in xrange(p, q):
        if (a[j] <= pivot):
            i += 1
            swap(a, i, j)
    swap(a, i+1, q)
    return i+1

def quicksort(a, p, r):
    if (p < r):
        pivot = partition(a, p, r)
        quicksort(a, p, pivot-1)
        quicksort(a, pivot+1, r)

def qsort(a):
    quicksort(a, 0, len(a) - 1)

arr = [1, 4, 3, 2, 4, 3, 6, 4]

qsort(arr)
print arr

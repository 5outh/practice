lcsMap = {}
lasti = 0
endstr = ""

def lcs(A,B):
    global lasti
    lasti = max( len(A), len(B) )
    return _lcs(A, B, len(A) - 1, len(B) - 1)

def _lcs(a, b, i, j):
    global lasti
    global endstr
    if(lcsMap.get((i,j)) is not None):
        return lcsMap[(i, j)]
    if(i < 0 or j < 0):
        return 0
    if (a[i] == b[j]):
        if(i < lasti):
            endstr = a[i] + endstr
            lasti = i
        soln = 1 + _lcs(a, b, i-1, j-1)
        lcsMap[(i, j)] = soln
        return soln
    else:
        soln = max(
            _lcs(a, b, i-1, j),
            _lcs(a, b, i, j-1)
            )
        lcsMap[(i, j)] = soln
        return soln

print lcs("ABCBDAB", "BDCABA")
print endstr

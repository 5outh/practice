def group(s):
    accum = []
    for char in s:
        if(accum and accum[-1][0] == char):
            accum[-1] = accum[-1] + char
        else:
            accum.append(char)
    return accum

def rle(s):
    gp = group(s)
    t = ""
    for l in gp:
        t = t + l[0]
        n = len(l)
        if(n != 1):
            t += str(n)
    return t

if __name__ == '__main__':
    print(rle("aabbcccddef"))
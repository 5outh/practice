dictionary = {}
select = {}

# select[(i, j)] = (char, next_select)

def lps(seq, i, j):
    global dictionary
    global select

    if(j < i):
        return 0

    if(dictionary.get((i, j)) != None):
        return dictionary[(i, j)]

    if(i == j):
        dictionary[(i, j)] = 1
        select[(i, j)] = (seq[i], None)
        return 1
    
    if(seq[i] == seq[j]):
        ans = 2 + lps(seq, i+1, j-1)
        select[(i, j)] = (seq[i], (i+1, j-1))
        dictionary[(i, j)] = ans
        return ans
    else:
        a = lps(seq, i+1, j)
        b = lps(seq, i, j-1)
        c = lps(seq, i+1, j-1)
        ans = max(a, b, c)

        if(ans == a):
            select[(i, j)] = ('', (i+1, j))
        elif(ans == b):
            select[(i, j)] = ('', (i, j-1))
        else:
            select[(i, j)] = ('', (i+1, j-1))

        dictionary[(i, j)] = ans

        return ans

def get_from_select(i, j, lgth):

    c, nxt = select[(i, j)]
    final_string = c

    while (nxt and select.get(nxt)):
        c, nxt = select[nxt]
        final_string += c

    if(lgth % 2 == 0):
        final_string += final_string[::-1]
    else:
        final_string += final_string[:-1][::-1]
    return final_string

def longest_palindromic_subsequence(seq):
    global dictionary, select
    longest = lps(seq, 0, len(seq)-1)
    print (longest)
    print (get_from_select(0, len(seq)-1, longest))
    dictionary = {}
    select = {}
import sys

test = "aabbbbababaaabbab"

"""
Find a) the first occurrence of b in string
     b) the longest list of only as in string, store final index
"""

def solution(string):
    firstB = string.find('b')
    print ((string, firstB))
    if(firstB == -1):
        return (0, 0)
    longestA = 0
    longestAIndex = 0
    currentA = 0
    currentAIndex = 0
    for i in range(firstB, len(string)):
        if (string[i] == 'a'):
            print ("found a", str(i))
            currentAIndex = i
            currentA += 1
        if(currentA > longestA):
            longestA = currentA
            longestAIndex = currentAIndex
        if(string[i] == 'b'):
            currentA = 0
    return (firstB, longestAIndex)
            

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        print(solution(sys.argv[1]))
    else:
        print(solution(test))


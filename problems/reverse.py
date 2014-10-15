def rev(xs):
    for i in range(len(xs)//2):
        xs[i], xs[-i-1] = xs[-i-1], xs[i]

if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5] 
    rev(xs)
    print(xs)
def squareGenerator(a,b):
    for i in range(a,b+1):
        yield i**2
print(*[x for x in squareGenerator(1, 10)], sep=',')
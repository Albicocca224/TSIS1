def tozeroGenerator(n):
    for i in reversed(range(1,n+1)):
        yield i
print(*[x for x in tozeroGenerator(10)], sep=',')
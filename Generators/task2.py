def evenGenerator(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
n=int(input())
print(*[x for x in evenGenerator(n)], sep=',')
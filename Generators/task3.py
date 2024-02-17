def divisibleGenerator(n):
    for i in range(1, n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i;
print(*[x for x in divisibleGenerator(20)], sep=',')
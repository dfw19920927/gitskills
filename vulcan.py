def trangle():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L + [0])]

#tr = trangle()
result = []
n = 0
for i in trangle():
    result.append(i)
    n= n + 1
    if n == 10:
        break

for r in result:
    print(r)
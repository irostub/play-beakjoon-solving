def fector(x: int):
    if x == 0:
        return 1
    else:
        return x * fector(x - 1)


N = int(input())
print(fector(N))
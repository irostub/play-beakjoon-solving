while True:
    k = int(input())
    if k == 0:
        exit()
    elif k == 1:
        print(1)
        continue
    n = k * 2
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    print(sieve[k + 1 : k * 2].count(True))
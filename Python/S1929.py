T1, T2 = map(int, input().split())
n = 1000001
sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i + i, n, i):
            sieve[j] = False

for i in range(T1, T2 + 1):
    if i == 1:
        continue
    if sieve[i]:
        print(i)
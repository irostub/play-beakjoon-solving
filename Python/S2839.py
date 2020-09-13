N = int(input())
S = 0
while True:
    if N % 5 == 0:
        print((N // 5) + S)
        break
    N -= 3
    S += 1
    if N < 0:
        print("-1")
        break
C = int(input())
for _ in range(C):
    K = list(map(int, input().split()))
    N = K.pop(0)
    cnt = 0
    for i in K:
        if i > sum(K) / N:
            cnt += 1
    print(format(cnt / N, ".3%"))
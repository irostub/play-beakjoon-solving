N, X = map(int, input().split())
A = list(map(int, input().split()))
for attr in A:
    if attr < X:
        print(attr, end=" ")

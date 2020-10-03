N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for attr in sorted(arr):
    print(attr)
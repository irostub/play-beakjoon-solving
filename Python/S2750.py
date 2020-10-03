N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for attr in arr:
    print(attr)
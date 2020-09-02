N = int(input())
arr = list(map(int, input().split()))
highScore = max(arr)
idx = 0
for i in arr:
    arr[idx] = i / highScore * 100
    idx += 1
print(sum(arr) / N)
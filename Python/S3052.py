arr = []
for _ in range(10):
    num = int(input()) % 42
    if num in arr:
        pass
    else:
        arr.append(num)
print(len(arr))
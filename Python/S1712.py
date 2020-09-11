A, B, C = map(int, (input().split()))
cnt = 1
if B >= C:
    print("-1")
else:
    print(A // (C - B) + 1)
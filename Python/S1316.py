cnt = 0
T = int(input())
for _ in range(T):
    S = input()
    if list(S) == sorted(S, key=lambda x: S.find(x)):
        cnt += 1
print(cnt)
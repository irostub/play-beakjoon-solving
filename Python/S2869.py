A, B, V = map(int, input().split())
S = (V - B) / (A - B)
if S == int(S):
    print(int(S))
else:
    print(int(S) + 1)
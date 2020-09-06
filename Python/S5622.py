S = input()
T = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0
for attr in S:
    re = 2
    for alphas in T:
        if attr in alphas:
            result += re + 1
            break
        re += 1
print(result)
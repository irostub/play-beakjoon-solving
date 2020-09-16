M = int(input())
N = int(input())
R = []
for i in range(M, N + 1):
    switcher = False
    if i != 0 and i != 1:
        for j in range(2, i):
            if i % j == 0:
                switcher = True
                break
        if not switcher:
            R.append(i)
if len(R) == 0:
    print("-1")
    exit()
print(sum(R))
print(min(R))
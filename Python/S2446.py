N = int(input())

for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    print("")
for i in range(N):
    if i == 0:
        continue
    for j in range(N - 1 - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print("")
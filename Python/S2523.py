N = int(input())
switch = False
x = 0
for i in range(2 * N - 1):
    if not switch:
        for j in range(i + 1):
            print("*", end="")
    if (i + 1) % N == 0 and i != 0:
        x = i + 1
        switch = True
    else:
        for j in range((i + 1) - ((i + 1) - x) * 2):
            print("*", end="")
    print("")
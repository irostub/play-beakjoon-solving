N = int(input())

for j in range(N):
    for i in range(N):
        if (i + 1) % 2 == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    for i in range(N):
        if (i + 1) % 2 == 1:
            print(" ", end="")
        else:
            print("*", end="")
    print("")
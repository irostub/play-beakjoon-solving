for _ in range(int(input())):
    R, S = list(input().split())
    for c in S:
        for _ in range(int(R)):
            print(c, end="")
    print("")
N = int(input())
S = input().split()
flag = 0
for attr in S:
    for attr2 in S:
        if attr == attr2:
            flag += 1
            pass
        elif attr != attr2:
            if attr[-1] == attr2[0]:
                flag += 1
if flag/len(S) == len(S):
    print(1)
else:
    print(0)
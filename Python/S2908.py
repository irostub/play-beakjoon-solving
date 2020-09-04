def switchNumber(a: str):
    temp = a[2:]
    temp += a[1:2]
    temp += a[0:1]
    return temp


S1, S2 = input().split()
newS1 = switchNumber(S1)
newS2 = switchNumber(S2)
print(max(int(newS1), int(newS2)))

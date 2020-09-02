def switchNumber(a: str):
    temp = a[0]
    a[0] = a[2]
    a[2] = temp
    return a


S1, S2 = input().split()
newS1 = switchNumber(S1)
newS2 = switchNumber(S2)
print(max(int(newS1), int(newS2)))
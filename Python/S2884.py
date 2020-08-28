H, M = map(int, input().split())
if M >= 45:
    M -= 45
elif H == 0 and M < 45:
    H = 23
    M = M + 15
elif H > 0 and M < 45:
    H -= 1
    M = M + 15
print(str(H) + " " + str(M))

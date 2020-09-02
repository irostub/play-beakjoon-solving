A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
for i in range(10):
    n = 0
    for j in range(len(result)):
        if int(result[j]) == i:
            n += 1
    print(n)
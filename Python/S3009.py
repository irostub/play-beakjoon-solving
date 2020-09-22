x = []
y = []
for _ in range(3):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
r1 = r2 = 0
for i in range(3):
    if x.count(x[i]) == 1:
        r1 = x[i]
    if y.count(y[i]) == 1:
        r2 = y[i]
print(str(r1) + " " + str(r2))
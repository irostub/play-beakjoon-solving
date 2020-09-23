X = int(input())
x = 1
y = 2
switcher = True
if X == 1:
    print("1/1")
    exit()

for _ in range(X - 2):
    if x == 1 and not switcher:
        y += 1
        switcher = True
    elif y == 1 and switcher:
        x += 1
        switcher = False
    elif switcher:
        x += 1
        y -= 1
    elif not switcher:
        x -= 1
        y += 1
print("%d/%d" % (x, y))
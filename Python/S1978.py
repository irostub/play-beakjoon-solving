N = int(input())
U = map(int, (input().split()))
count = 0
for attr in U:
    switcher = False
    if attr != 1 and attr != 0:
        for i in range(2, attr):
            if attr % i == 0:
                switcher = True
        if not switcher:
            count += 1
print(count)
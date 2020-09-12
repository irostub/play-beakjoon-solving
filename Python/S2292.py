N = int(input())
x = 1
k = 1
s = 1
while True:
    n = s
    s = s + (6 * x)
    if N != 1 and N > k and N <= s:
        print(x + 1)
        break
    elif N == 1:
        print("1")
        break
    x += 1
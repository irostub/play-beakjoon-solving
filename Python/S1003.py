nazi = {0:0, 1:1}
def fibonacci(n):
    if n in nazi:
        return nazi[n]

    nazi[n] = fibonacci(n-1) + fibonacci(n-2)
    return nazi[n]
        
T = int(input())

for _ in range(T):
    X = int(input())
    fibonacci(X)
    if X != 0:
        print(str(nazi[X-1])+" "+str(nazi[X]))
    elif X == 0:
        print("1 0")
    nazi = {0:0, 1:1}
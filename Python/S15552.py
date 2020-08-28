import sys

T = int(input())
for _ in range(T):
    A, B = sys.stdin.readline().strip().split()
    print(int(A) + int(B))

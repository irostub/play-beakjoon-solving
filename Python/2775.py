for _ in range(int(input())):
  k = int(input())
  n = int(input())

  zero = [i for i in range(1,n+1)]

  for i in range(k):
    for j in range(1, n):
      zero[j] += zero[j-1]

  print(zero[-1])
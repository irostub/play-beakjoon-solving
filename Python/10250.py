for _ in range(int(input())):
  H, W, N = map(int, input().split())
  Y = 0
  X = 0
  if N % H == 0:
    Y = H*100
    X = N // H
  else:
    Y = (N % H) * 100
    X = N // H + 1
    
  print(Y + X)
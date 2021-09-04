T = int(input())
for _ in range(T):
  arr = list(input().split())
  if arr[0][-1] == "1":
    print(1)
  elif arr[0][-1] == "0":
    print(10)
  elif arr[0][-1] == "2":
    if int(arr[1])%4 == 0:
      print(6)
    elif int(arr[1])%4 == 1:
      print(2)
    elif int(arr[1])%4 == 2:
      print(4)
    else:
      print(8)
  elif arr[0][-1] == "3":
    if int(arr[1])%4 == 0:
      print(1)
    elif int(arr[1])%4 == 1:
      print(3)
    elif int(arr[1])%4 == 2:
      print(9)
    else:
      print(7)
  elif arr[0][-1] == "4":
    if int(arr[1])%2 == 1:
      print(4)
    else:
      print(6)
  elif arr[0][-1] == "5":
    print(5)
  elif arr[0][-1] == "6":
    print(6)
  elif arr[0][-1] == "7":
    if int(arr[1])%4 == 0:
      print(1)
    elif int(arr[1])%4 == 1:
      print(7)
    elif int(arr[1])%4 == 2:
      print(9)      
    else:
      print(3)
  elif arr[0][-1] == "8":
    if int(arr[1])%4 == 0:
      print(6)
    elif int(arr[1])%4 == 1:
      print(8)
    elif int(arr[1])%4 == 2:
      print(4)
    else:
      print(2)
  elif arr[0][-1] == "9":
    if int(arr[1])%2 == 1:
      print(9)
    else:
      print(1)
  
    

X = int(input())

count = 1
while X > count:
  X -= count
  count += 1

cardinal = 0
ordinal = 0

if count % 2 == 0:
  cardinal=X
  ordinal=count-X+1
else:
  cardinal=count-X+1
  ordinal=X

print(cardinal,"/",ordinal,sep="")
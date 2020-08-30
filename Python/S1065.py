def check_num(num):
    if num < 100:
        return True
    else:
        splitNum = str(num)
        cd = int(splitNum[0]) - int(splitNum[1])
        for i in range(1, len(splitNum) - 1):
            if cd != int(splitNum[i]) - int(splitNum[i + 1]):
                return False
        return True


cnt = 0
for i in range(1, int(input()) + 1):
    if check_num(i):
        cnt += 1
print(cnt)
nums = set(range(1, 10001))


def d(nums):
    genNums = set()
    for i in nums:
        temp = i
        for j in str(i):
            temp += int(j)
        genNums.add(temp)
    for i in sorted(nums.difference(genNums)):
        print(i)


d(nums)
N = input()
count = 0
if int(N) < 10:
    N = "0" + N
switch = True
newNumber = ""
while newNumber != N:
    if switch:
        n_sum = str(int(N[0]) + int(N[1]))
        newNumber = N[len(N) - 1] + n_sum[len(n_sum) - 1]
        switch = False
    else:
        n_sum = str(int(newNumber[0]) + int(newNumber[1]))
        newNumber = newNumber[len(newNumber) - 1] + n_sum[len(n_sum) - 1]
    count += 1
print(count)
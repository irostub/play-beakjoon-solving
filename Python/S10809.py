dic = {}
S = input()
for j in range(26):
    try:
        dic[j] = S.index(chr(j + 97))
    except ValueError as e:
        dic[j] = -1
values = dic.values()
for value in values:
    print(str(value) + " ", end="")
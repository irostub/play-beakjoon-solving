s = input()
l = []
for i in range(26):
    l.append(s.count(chr(65 + i)) + s.count(chr(97 + i)))
maxValue = l.index(max(l))
maxCount = l.pop(maxValue)
if maxCount in l:
    print("?")
else:
    print(chr(maxValue + 65))
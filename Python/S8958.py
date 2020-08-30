N = int(input())
for _ in range(N):
    card = list(input())
    score = 0
    temp = 0
    for i in card:
        if i == "O":
            temp += 1
            score += temp
        elif i == "X":
            temp = 0
            score += temp
    print(score)
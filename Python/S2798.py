N, M = map(int, input().split())
cards = map(int, input().split())
available = [attr for attr in cards if attr <= M]
topCard = 0
for j in range(len(available)):
    for k in range(j + 1, len(available)):
        for l in range(k + 1, len(available)):
            if (available[j] + available[k] + available[l]) <= M:
                topCard = max(topCard, available[j] + available[k] + available[l])
print(topCard)
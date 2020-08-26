import math
for _ in range (int(input())):
    posInput = tuple(map(int, input().split()))
    startPos = posInput[:2]
    endPos = posInput[2:]
    planets = []
    for _ in range(int(input())):
        planets.append(tuple(map(int, input().split())))
    count = 0
    for planet in planets:
        startPointDist = math.sqrt(math.pow(startPos[0] - planet[0],2)+math.pow(startPos[1]-planet[1],2))
        endPointDist = math.sqrt(math.pow(endPos[0] - planet[0],2)+math.pow(endPos[1]-planet[1],2))
        if startPointDist < planet[2] and endPointDist < planet[2]:
            pass
        elif startPointDist < planet[2] and endPointDist > planet[2] or startPointDist > planet[2] and endPointDist < planet[2]:
            count += 1 
    print(count)
class Person:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_distance = 0

import math

class Main:
    p1, p2 = Person(), Person()
    T = int(input())
    for _ in range(T):
        p1.x, p1.y, p1.target_distance, p2.x, p2.y, p2.target_distance = map(int,input().split())
        dist = math.sqrt(math.pow(p2.x-p1.x,2)+math.pow(p2.y-p1.y,2))
        r_sum, r_sub = p2.target_distance + p1.target_distance, abs(p2.target_distance - p1.target_distance)
        if dist == 0:
            if p1.target_distance == p2.target_distance:
                print("-1", sep='\n')
            else:
                print("0", sep='\n')
        elif dist == r_sum or dist == r_sub:
            print("1", sep='\n')
        elif dist < r_sum and dist > r_sub:
            print("2", sep='\n')
        elif dist > r_sum or dist < r_sub:
            print("0", sep='\n')
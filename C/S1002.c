#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Person
{
    int x;
    int y;
    int target_distance;
};

int main(void)
{
    struct Person p1, p2;
    int loopControl = 0;
    scanf("%d", &loopControl);
    while (loopControl > 0)
    {
        scanf("%d %d %d %d %d %d", &p1.x, &p1.y, &p1.target_distance, &p2.x, &p2.y, &p2.target_distance);

        double distance = sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
        int r_sum = p2.target_distance + p1.target_distance;
        int r_sub = abs(p2.target_distance - p1.target_distance);

        if (distance == 0)
        {
            if (p1.target_distance == p2.target_distance)
            {
                printf("-1\n");
            }
            else
            {
                printf("0\n");
            }
        }
        else if (distance == r_sum || distance == r_sub)
        {
            printf("1\n");
        }
        else if (distance < r_sum && distance > r_sub)
        {
            printf("2\n");
        }
        else if (distance > r_sum || distance < r_sub)
        {
            printf("0\n");
        }
        loopControl--;
    }
}
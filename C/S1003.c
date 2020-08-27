#include <stdio.h>

int nazi[41] = {0,1};

int fibonacci(int n)
{
    if (n < 0)
        return 0;
    if (nazi[n] != 0)
    {
        return nazi[n];
    }
    nazi[n] = fibonacci(n-1) + fibonacci(n-2);
    return nazi[n];
}
int main(void)
{
    int T;
    scanf("%d", &T);

    for(int i = 0; i<T; i++)
    {
        int X;
        scanf("%d", &X);
        if (X == 0)
        {
            printf("1 0\n");
            continue;
        }
        else if (X == 1)
        {
            printf("0 1\n");
            continue;
        }
        fibonacci(X);
        if (X != 0)
        printf("%d %d\n",nazi[X-1],nazi[X]);
    }
}
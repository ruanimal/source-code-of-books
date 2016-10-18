#include <stdio.h>

struct note {
    int x;
    int y;
};

int main() {
    struct note que[2501];
    int head, tail;
    int a[51][51];
    int book[51][51] = {0};
    int i, j, k, sum, max=0, mx, my, n, m, startx, starty, tx, ty;
    int next[4][2] = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0},
    };
    scanf("%d %d %d %d", &n, &m, &startx, &starty);
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    head = 1;
    tail = 1;
    que[tail].x = startx;
    que[tail].y = starty;
    tail++;
    book[startx][starty] = 1;
    sum = 1;
    while (head<tail) {
        for (k=0; k<=3; k++) {
            tx=que[head].x + next[k][0];
            ty=que[head].y + next[k][1];
            if (tx<1 || tx>n || ty<1 || ty>m) {
                continue;
            }
            if (a[tx][ty] > 0 && book[tx][ty] == 0) {
                sum++;
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                tail++;
            }
        }
        head++;
    }
    printf("land size: %d\n", sum);
    getchar();
    return  0;
}

/* input
10 10 6 8
1 2 1 0 0 0 0 0 2 3
3 0 2 0 1 2 1 0 1 2
4 0 1 0 1 2 3 2 0 1
3 2 0 0 0 1 2 4 0 0
0 0 0 0 0 0 1 5 3 0
0 1 2 1 0 1 5 4 3 0
0 1 2 3 1 3 6 2 1 0
0 0 3 4 8 9 7 5 0 0
0 0 0 3 7 8 6 0 1 2
0 0 0 0 0 0 0 0 1 0

* output
land size: 38
*/
#include <stdio.h>


int a[51][51];
int book[51][51], n, m, sum;
void dfs(int x, int y, int color) {
    int next[4][2] = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0},
    };
    int k, tx, ty;
    a[x][y] = color;
    for (k=0; k<=3; k++) {
        tx = x + next[k][0];
        ty = y + next[k][1];
        if (tx<1 || tx>n || ty<1 || ty>m) {
            continue;
        }
        if (a[tx][ty] > 0 && book[tx][ty] == 0) {
            sum++;
            book[tx][ty] = 1;
            dfs(tx, ty, color);
        }
    }
}

int main() {
    int i, j, startx, starty;
    scanf("%d %d %d %d", &n, &m, &startx, &starty);
    for (i=1; i<=n; i++) {
        for (j=1; j<=m; j++) {
            scanf("%d", &a[i][j]);
        }
    }
    book[startx][starty] = 1;
    sum = 1;
    dfs(startx, starty, -1);
    for (i=1; i<=n; i++) {
        for (j=1; j<=m; j++) {
            printf("%3d", a[i][j]);
        }
        printf("\n");
    }
    getchar();
    return 0;
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
  1  2  1  0  0  0  0  0  2  3
  3  0  2  0 -1 -1 -1  0  1  2
  4  0  1  0 -1 -1 -1 -1  0  1
  3  2  0  0  0 -1 -1 -1  0  0
  0  0  0  0  0  0 -1 -1 -1  0
  0 -1 -1 -1  0 -1 -1 -1 -1  0
  0 -1 -1 -1 -1 -1 -1 -1 -1  0
  0  0 -1 -1 -1 -1 -1 -1  0  0
  0  0  0 -1 -1 -1 -1  0  1  2
  0  0  0  0  0  0  0  0  1  0
*/
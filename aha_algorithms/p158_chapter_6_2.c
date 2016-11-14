#include <stdio.h>

int main() {
    int e[10][10], dis[10], book[10], i, j, n, m, t1, t2, t3, u, v, min;
    int inf = 99999999;
    scanf("%d %d", &n, &m);
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            if (i==j) {
                e[i][j] = 0;
            } else {
                e[i][j] = inf;
            }
        }
    }

    for (i=1; i<=m; i++) {
        scanf("%d %d %d", &t1, &t2, &t3);
        e[t1][t2] = t3;
    }

    for (i=1; i<=n; i++) {
        dis[i] = e[1][i];
    }
    for (i=1; i<=n; i++) {
        book[i] = 0;
    }
    book[1] = 1;

    for (i=1; i<=n-1; i++) {
        min = inf;
        for (j=1; j<=n; j++) {
            if (book[j]==0 && dis[j]<min) {
                min = dis[j];
                u = j;
            }
        }
        book[u] = 1;
        for (v=1; v<=n; v++) {
            if (e[u][v]<inf) {
                if (dis[v]>dis[u]+e[u][v]) {
                    dis[v] = dis[u] + e[u][v];
                }
            }
        }
    }

    for (i=1; i<=n; i++) {
        printf("%d ", dis[i]);
    }

    getchar();
    return 0;
}

/* input
6 9
1 2 1
1 3 12
2 3 9
2 4 3
3 5 5
4 3 4
4 5 13
4 6 15
5 6 4

* output
0 1 8 4 13 17
 */
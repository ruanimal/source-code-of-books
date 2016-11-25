#include <stdio.h>

int main() {
    int dis[10], i, k, n, m, u[10], v[10], w[10], check, flag;
    int inf = 99999999;
    scanf("%d %d", &n, &m);
    for (i=1; i<=m; i++) {
        scanf("%d %d %d", &u[i], &v[i], &w[i]);
    }
    for (i=1; i<=m; i++) {
        dis[i] = inf;
    }
    dis[1] = 0;

    for (k=1; k<=n-1; k++) {
        check = 0;
        for (i=1; i<=m; i++) {
            if (dis[v[i]] > dis[u[i]] + w[i]) {
                dis[v[i]] = dis[u[i]] + w[i];
                check = 1;
            }
        }
        if (check == 0) {
            break;
        }
    }

    flag = 0;
    for (i=1; i<=m; i++) {
        if (dis[v[i]] > dis[u[i]] + w[i]) {
            flag = 1;
            break;
        }
    }

    if (flag == 1) {
        printf("此图含有负权回路");
    } else {
        for (i=1; i<=n; i++) {
            printf("%d ", dis[i]);
        }
    }

    getchar();
    return 0;
}

/* input
5 5
2 3 2
1 2 -3
1 5 5
4 5 2
3 4 3
* output
0 -3 -1 2 4
 */
#include <stdio.h>

int main() {
    int n, m, i, j, k;
    int u[8], v[8], w[8];
    int first[6], next[8];
    int dis[6] = {0}, book[6] = {0};
    int que[101] = {0}, head = 1, tail = 1;
    int inf = 99999999;
    scanf("%d %d", &n, &m);
    for (i=1; i<=n; i++) {
        dis[i] = inf;
        book[i] = 0;
        first[i] = -1;
    }
    dis[1] = 0;

    for (i=1; i<=m; i++) {
        scanf("%d %d %d", &u[i], &v[i], &w[i]);
        next[i] = first[u[i]];
        first[u[i]] = i;
    }
    que[tail] = 1;
    tail++;
    book[1] = 1;
    while (head<tail) {
        k = first[que[head]];
        while (k != -1) {
            if (dis[v[k]]>dis[u[k]]+w[k]) {
                dis[v[k]] = dis[u[k]] + w[k];
                if (book[v[k]] == 0) {
                    que[tail] = v[k];
                    tail++;
                    book[v[k]]=1;
                }
            }
            k=next[k];
        }
        book[que[head]]=0;
        head++;
    }

    for (i=1; i<=n; i++) {
        printf("%d ", dis[i]);
    }

    getchar();
    return 0;
}

/* input
5 7
1 2 2
1 5 10
2 3 3
2 5 7
3 4 4
4 5 5
5 3 6
* output
0 2 5 9 9
 */
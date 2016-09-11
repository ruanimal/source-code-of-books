# -*- coding:utf-8 -*-

minimal = 999999
n, m = (5, 4)
startx, starty, p, q = (1, 1, 4, 3)
a = [[None for i in range(7)] for j in range(7)]
book = [[0 for i in range(7)] for j in range(7)]


def dfs(x, y, step):
    global minimal
    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    if (x==p and y==q):
        if step < minimal:
            minimal = step
        return

    for k in range(4):
        tx = x + _next[k][0]
        ty = y + _next[k][1]
        if tx<1 or tx>n or ty<1 or ty>m:
            continue
        if a[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1
            dfs(tx, ty, step+1)
            book[tx][ty] = 0


def main():
    maze_map = iter((
        '0 0 1 0 '
        '0 0 0 0 '
        '0 0 1 0 '
        '0 1 0 0 '
        '0 0 0 1 '
    ).split())
    for i in range(1, n+1):
        for j in range(1, m+1):
            a[i][j] = int(maze_map.next())
    book[startx][starty] = 1
    dfs(startx, starty, 0)
    print minimal

main()

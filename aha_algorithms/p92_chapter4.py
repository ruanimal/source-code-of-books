# -*- coding:utf-8 -*-
#!/usr/bin/env python

class Note(object):
    pass

que = [Note() for _ in range(2501)]

a = [[0 for i in range(51)] for j in range(51)]
book = [[0 for i in range(51)] for j in range(51)]

_next = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]

n, m = (5, 4)
_tmp = [int(i) for i in '0 0 1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1'.split()]
for i in range(1, n+1):
    for j in range(1, m+1):
        a[i][j] = _tmp.pop(0)
startx, starty, p, q = 1, 1, 4, 3
head = tail = 1
que[tail].x = startx
que[tail].y = starty
que[tail].f = 0
que[tail].s = 0
tail += 1
book[startx][starty] = 1

flag = 0
while head<tail:
    for k in range(4):
        tx = que[head].x + _next[k][0]
        ty = que[head].y + _next[k][1]
        print tx, ty
        if tx<1 or tx>n or ty<1 or ty>m:
            continue
        if a[tx][ty] == 0 and book[tx][ty] ==0:
            book[tx][ty] = 1
            que[tail].x = tx
            que[tail].y = ty
            que[tail].f = head
            que[tail].s = que[head].s + 1
            tail += 1
        if tx == p and ty == q:
            flag = 1
            break
    if flag == 1:
        break
    head += 1

print que[tail-1].s

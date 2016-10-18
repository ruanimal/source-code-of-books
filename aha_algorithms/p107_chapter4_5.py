#!/usr/bin/env python
# -*- coding:utf-8 -*-


land_map = """
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
"""
land_map = [[int(j) for j in i.split(' ')]for i in land_map.split('\n') if i]
book = [[0 for i in range(10)] for j in range(10)]
class Note(object): pass

def main():
    que = [Note() for _ in range(200)]
    edge, startx, starty, _sum = (10, 5, 7, 1)
    head = tail = 1
    que[tail].x = startx
    que[tail].y = starty
    tail += 1
    book[startx][starty] = 1
    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    while head < tail:
        for i in range(4):
            tx = que[head].x + _next[i][0]
            ty = que[head].y + _next[i][1]
            if tx<0 or tx>edge-1 or ty<0 or ty>edge-1:
                continue
            if land_map[tx][ty] > 0 and book[tx][ty] == 0:
                _sum += 1
                book[tx][ty] = 1
                que[tail].x = tx
                que[tail].y = ty
                tail += 1
        head += 1
    print "land size: %d" % _sum


main()

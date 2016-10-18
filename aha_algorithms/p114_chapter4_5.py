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
_sum = 1

def dfs(x, y, color):
    global _sum
    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    land_map[x][y] = color
    for i in range(4):
        tx = x + _next[i][0]
        ty = y + _next[i][1]
        if tx<0 or tx>edge-1 or ty<0 or ty>edge-1:
            continue
        if land_map[tx][ty] > 0 and book[tx][ty] == 0:
            _sum += 1
            book[tx][ty] = 1
            dfs(tx, ty, color)

edge = 10
color = 0
for i in range(edge):
    for j in range(edge):
        if land_map[i][j] > 0:
            color -= 1
            book[i][j] = 1
            dfs(i, j, color)
for i in land_map:
    for j in i:
        print "%3d" % j,
    print '\n'

print "have %d island!" % -color

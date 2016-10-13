#!/usr/bin/env python
# -*- coding:utf-8 -*-

game_map = """
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.#.#
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############"""

game_map = [list(i) for i in game_map.split()]
book = [[0 for i in range(20)] for j in range(20)]
edge, startx, starty = (13, 3, 3)

def getnum(note_x, note_y):
    _sum = 0
    for i in range(note_x-1, -1, -1):
        if game_map[i][note_y] == '#':
            break
        elif game_map[i][note_y] == 'G':
            _sum += 1

    for i in range(note_x, edge):
        if game_map[i][note_y] == '#':
            break
        elif game_map[i][note_y] == 'G':
            _sum += 1

    for i in range(note_y-1, -1, -1):
        if game_map[note_x][i] == '#':
            break
        elif game_map[note_x][i] == 'G':
            _sum += 1

    for i in range(note_y, edge):
        if game_map[note_x][i] == '#':
            break
        elif game_map[note_x][i] == 'G':
            _sum += 1

    return _sum

_max = mx = my = 0

def dfs(x, y):
    global _max, mx, my
    _sum = getnum(x, y)
    if (_max < _sum):
        mx = x
        my = y
        _max = _sum

    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    for dx, dy in _next:
        tx = x + dx
        ty = y + dy
        if tx<0 or tx>edge-1 or ty<0 or ty>edge-1:
            continue
        if game_map[tx][ty] == '.' and book[tx][ty] == 0:
            book[tx][ty] = 1
            dfs(tx, ty)


def main():
    global _max, mx, my
    book[startx][starty] = 1
    _max = getnum(startx, starty)
    mx = startx
    my = starty
    dfs(startx, starty)
    print "location (%d, %d), kill %d enemy.\n" % (mx, my, _max)


main()


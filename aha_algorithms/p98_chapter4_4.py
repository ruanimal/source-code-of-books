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
edge, startx, starty = (13, 3, 3)

class Note(object):
    def __init__(self, x, y, num=0):
        self.x = x
        self.y = y
        self.num = num


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


def main():
    que = [Note(0, 0) for _ in range(401)]
    _max = Note(0, 0, 0)
    book = [[0 for i in range(20)] for j in range(20)]
    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    head = tail = 1
    que[tail] = Note(startx, starty, getnum(startx, starty))
    tail += 1
    book[startx][starty] = 1

    while head<tail:
        for dx, dy in _next:
            tx = que[head].x + dx
            ty = que[head].y + dy
            if tx<0 or tx>edge-1 or ty<0 or ty>edge-1:
                continue
            if game_map[tx][ty] == '.' and book[tx][ty] == 0:
                book[tx][ty] = 1
                que[tail] = Note(tx, ty, getnum(tx, ty))
                if _max.num < que[tail].num:
                    _max = que[tail]
                tail += 1
        head += 1
    print "location (%d, %d), kill %d enemy.\n" % (_max.x, _max.y, _max.num)

main()

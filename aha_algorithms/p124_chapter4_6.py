#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 水管类型  1:┗, 2:┏, 3:┓, 4:┛, 4:--, 6:|
# 水流方向  1:left, 2:top, 3:right, 4:down

class Note(object): pass

stack = [Note() for _ in range(100)]
game_map = """
5 3 5 3
1 5 3 0
2 3 5 1
6 1 1 5
1 5 5 4
"""
game_map = [[int(j) for j in i.split()] for i in game_map.split('\n') if i]
book = [[0 for i in range(10)] for j in range(10)]
n, m, flag, top = (4, 3, 0, 0)  # 从0开始

def dfs(x, y, front):
    global flag, top
    if x==n and y==m+1:
        flag = 1
        for i in range(1, top+1):
            print '(%d, %d)' % (stack[i].x+1, stack[i].y+1),
        return

    if x<0 or x>n or y<0 or y>m:
        return

    if book[x][y] == 1:
        return

    book[x][y] = 1
    top += 1
    stack[top].x = x
    stack[top].y = y
    if game_map[x][y]>=5 and game_map[x][y]<=6:
        if (front==1):
            dfs(x, y+1, 1);
        if (front==2):
            dfs(x+1, y, 2);
        if (front==3):
            dfs(x, y-1, 3);
        if (front==4):
            dfs(x-1, y, 4);
    if game_map[x][y]>=1 and game_map[x][y]<=4:
        if (front==1):
            dfs(x+1, y, 2);
            dfs(x-1, y, 4);
        if (front==2):
            dfs(x, y+1, 1);
            dfs(x, y-1, 3);
        if (front==3):
            dfs(x-1, y, 4);
            dfs(x+1, y, 2);
        if (front==4):
            dfs(x, y+1, 1);
            dfs(x, y-1, 3);
    book[x][y] = 0
    top -= 1


def main():
    num = 0
    dfs(0, 0, 1)
    if flag==0:
        print("imporssible")

main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

_input = """
5 5
1 2
1 3
1 5
2 4
3 5
"""
book = [0 for i in range(100)]
que = [0 for i in range(10001)]
n = m = 5
_sum = 0

book = [0 for _ in range(10)]
_map = [[0 if i==j else 99999999 for i in range(6) ] for j in range(6)]
for i in _input.split('\n'):
    if not i.strip(): continue
    a, b = i.split()
    _map[int(a)][int(b)] = 1;
    _map[int(b)][int(a)] = 1;

head = tail = 1
que[tail] = 1
book[tail] = 1
tail += 1

while head < tail:
    cur = que[head]
    for i in range(1, n+1):
        if (_map[cur][i] == 1 and book[i] == 0):
            que[tail] = i
            tail += 1
            book[i] = 1
        if tail > n:
            break
    head += 1

for i in range(1, n+1):
    print que[i],

#!/usr/bin/env python3
lst = []
with open('entry.txt') as f:
    for x in f:
        lst.append(int(x.strip()))

for num in lst:
    for num2 in lst:
        for num3 in lst:
            if num + num2 + num3 == 2020:
                print(num * num2 * num3)
                break
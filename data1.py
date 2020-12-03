#!/usr/bin/env python3
import re
file = open('data1.txt')
nums = 0
for line in file:
    line = line.rstrip()
    nums = nums + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

print(nums)
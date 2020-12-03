#!/usr/bin/env python3
right = 3
tree = 0
count = 0
with open('entry3_test.txt') as file:
    for line in file:
        print(line)
        print(line[right])
        #if count == 0:
         #   pass
        #elif line[right] == '#':
        #    tree += 1
        if (len(line) - right) >= 3:
            right += 3
        #count += 1
        #print(right)
print(tree)
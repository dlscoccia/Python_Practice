#!/usr/bin/python3
x = 0
y = 0
for a in range(1,1001):
    if (a%2==0) | (a%3==0):
        print(a)
        x += 1
        
for a in range(1,1001):
    if (a%2!=0) & (a%3!=0):
        print(a)
        y += 1
print(x, y)
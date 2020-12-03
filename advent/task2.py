#!/usr/bin/env python3
pass_count = 0
pass_list = []
range1 = 0
range2 = 0
line = []
args = []
char = ''
passs = ""
char_count = 0
with open('entry2.txt') as file:
    for line in file:
        pass_list.append(line.strip())
for pass_line in pass_list:
    line = pass_line.split()
    args = line[0].split('-')
    range1 = int(args[0]) - 1
    range2 = int(args[1]) - 1
    char = line[1].strip(':')
    passs = line[2]
    if passs[range1] == char and passs[range2] == char:
        pass
    elif passs[range1] == char and passs[range2] != char:
        pass_count += 1
    elif passs[range1] != char and passs[range2] == char:
        pass_count += 1
print(pass_count)
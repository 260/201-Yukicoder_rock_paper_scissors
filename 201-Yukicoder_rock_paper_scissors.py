#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/436

first_line  = input()
second_line = input()

point_A = first_line.split(' ')[1]
point_B = second_line.split(' ')[1]

if len(point_A) == len(point_B):
    if point_A == point_B:
        print(-1)
    elif point_A > point_B:
        print(first_line.split(' ')[0])
    else:
        print(second_line.split(' ')[0])
elif len(point_A) > len(point_B):
    print(first_line.split(' ')[0])
else:
    print(second_line.split(' ')[0])

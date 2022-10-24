import math
def point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print((math.floor(x1), math.floor(y1)))
    else:
        print((math.floor(x2), math.floor(y2)))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point(x1, y1, x2, y2)

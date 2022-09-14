import sys
D = int(input())
B = int(input())
max_num = -sys.maxsize
for i in range(B+1):
    if i > max_num and i % D == 0:
        max_num = i
print(max_num)


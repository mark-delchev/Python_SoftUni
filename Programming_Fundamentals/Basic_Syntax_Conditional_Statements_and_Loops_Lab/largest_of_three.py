import sys
largest_num = (-sys.maxsize)
for i in range(3):
    num = int(input())
    if num > largest_num:
        largest_num = num
print(largest_num)
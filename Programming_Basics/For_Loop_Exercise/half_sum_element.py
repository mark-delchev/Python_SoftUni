import sys
n = int(input())
sum_number = 0
max_number = -sys.maxsize
for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_number += num

if max_number == sum_number - max_number:
    print('Yes')
    print(f'Sum = {sum_number - max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - (sum_number - max_number))}')



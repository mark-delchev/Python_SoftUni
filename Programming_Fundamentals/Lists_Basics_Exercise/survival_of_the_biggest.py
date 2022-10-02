from cgitb import small
import sys
num_lst = input().split(" ")
nums_to_remove = int(input())

smallest_num = sys.maxsize

for i in num_lst:
    if int(i) < smallest_num:
        smallest_num = int(i)
        num_lst.remove(str(smallest_num))

for i in num_lst:
    print(int(i), end=" ")
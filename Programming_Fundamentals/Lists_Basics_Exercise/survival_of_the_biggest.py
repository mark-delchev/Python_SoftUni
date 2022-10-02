num_lst = input().split(" ")
num_lst_int = [eval(i) for i in num_lst]
nums_to_remove = int(input())

num_lst_int.sort()

for i in range(nums_to_remove):
    num_lst.remove(str(num_lst_int[i]))


for i in num_lst:
    if i == num_lst[-1]:
        print(int(i))
    else:
        print(int(i), end=", ")
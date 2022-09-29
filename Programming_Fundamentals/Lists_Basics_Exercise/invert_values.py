nums = input()
num_list = []
new_list = []
num_list = nums.split(sep = " ")

for i in num_list:
    new_num = (int(i)) * -1
    new_list.append(new_num)

print(new_list)


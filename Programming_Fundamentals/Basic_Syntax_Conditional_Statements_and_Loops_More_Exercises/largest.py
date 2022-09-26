num = int(input())
largest_num = 0
num_list = []
for i in str(num):
    digit = int(i)
    num_list.append(digit)
num_list_final = sorted(num_list, reverse=True)
print(*num_list_final, sep="")

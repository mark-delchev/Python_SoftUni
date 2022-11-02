lst = input().split(", ")
lst2 = input().split(", ")
final_lst = []

for i in lst:
    for k in lst2:
        if i in k and i not in final_lst:
            final_lst.append(i)


print(final_lst)

lst = list(input().split(sep=", "))
beggars = int(input())
beggars_lst = []
even_sum = 0
odd_sum = 0

for i in range(len(lst)):
    even_sum = 0
    odd_sum = 0
    for i in range(beggars):
        if i % 2 == 0:
            even_sum += int(lst[i])
        else:
            odd_sum += int(lst[i])
    beggars_lst.append(int(lst[i]))

print(odd_sum)
print(even_sum)







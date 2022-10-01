lst = list(input().split(sep=", "))
beggars_lst = [0] * int(input())

for i in range(len(lst)):
    for j in range(len(beggars_lst)):
        try:
            if int(lst[i]) % int(beggars_lst[j]) == 0:
                beggars_lst[j] = (int(lst[i]) + int(lst[i + 2]))
        except IndexError:
            break

print(beggars_lst)








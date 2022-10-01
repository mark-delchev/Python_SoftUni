lst = input().split(sep=", ")
lst_int = [eval(i) for i in lst]

beggars = int(input())
beggars_lst = []
counter = 0


while counter < beggars:
    current_beggar = 0
    for i in range(counter, len(lst_int), beggars):
        current_beggar += lst_int[i]
    beggars_lst.append(current_beggar)
    counter += 1

            


print(beggars_lst)










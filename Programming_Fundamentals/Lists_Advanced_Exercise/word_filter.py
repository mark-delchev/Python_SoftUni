lst = input().split(" ")
lst_final = [i for i in lst if len(i) % 2 == 0]
for i in lst_final:
    print(i)
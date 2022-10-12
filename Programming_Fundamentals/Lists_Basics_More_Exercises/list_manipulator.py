

lst = input().split(" ")

while True:
    command = input().split(" ")
    if command == ["end"]:
        break
    if command[0] == "exchange":
        indx = int(command[1])
        lst1 = lst[indx:]
        lst2 = lst[:indx]
        final_lst = lst1 + lst2
        print(lst1)
        print(lst2)
        print(final_lst)

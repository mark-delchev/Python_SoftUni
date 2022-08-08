number = int(input())
for i in range(1111, 9999 + 1):
    special_num = True
    string_i = str(i)
    for j in string_i:
        if string_i[0] == "0" or string_i[1] == "0" or string_i[2] == "0" or string_i[3] == "0":
            special_num = False
    if special_num:
        if number % int(string_i[0]) == 0 and \
                number % int(string_i[1]) == 0 and \
                number % int(string_i[2]) == 0 and \
                number % int(string_i[3]) == 0:
            print(i, end=" ")

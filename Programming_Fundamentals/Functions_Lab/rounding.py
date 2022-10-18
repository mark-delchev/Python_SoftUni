def rounding(inpt):
    lst = inpt.split(" ")
    lst_float = [float(i) for i in lst]
    lst_round = []
    for i in lst_float:
        lst_round.append(round(i))
    return lst_round

data = input()
print(rounding(data))



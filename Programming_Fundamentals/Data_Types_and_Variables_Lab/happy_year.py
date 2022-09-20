year = int(input())
next_year = year
next_year_str = []
year_found = False

while not year_found:
    next_year += 1
    for i in str(next_year):
        if i not in next_year_str:
            next_year_str.append(i)
            continue
        elif i in next_year_str:
            next_year_str = []
            break
    if next_year_str != []:
        year_found = True
print(next_year)





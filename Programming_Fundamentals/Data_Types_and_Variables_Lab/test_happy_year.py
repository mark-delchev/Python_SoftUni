year_found = True
next_year_str = []
next_year = 1022

for i in str(next_year):
    if i not in next_year_str:
        next_year_str.append(i)
        continue
    elif i in next_year_str:
        year_found = False
        next_year_str = []    
        break
print(year_found)
print(next_year_str)


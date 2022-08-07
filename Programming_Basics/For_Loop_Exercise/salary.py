opened_tabs = int(input())
salary = int(input())
fine = 0

for i in range(1, opened_tabs + 1):
    try:
        tab = input()
    except EOFError:
        tab = ''
    if tab == 'Facebook':
        fine += 150
    elif tab == 'Instagram':
        fine += 100
    elif tab == 'Reddit':
        fine += 50
    elif tab == '':
        fine += 0
if salary - fine <= 0:
    print('You have lost your salary.')
else:
    print(salary - fine)
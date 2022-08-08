name = input()
years_counter = 0
failed_counter = 0
grades_counter = 0
while True:
    years_counter += 1
    mark = float(input())
    if mark < 4.00:
        failed_counter += 1
    else:
        grades_counter += 1
    if failed_counter == 2:
        print(f'{name} has been excluded at {years_counter - 1} grade')
        break
    if years_counter == 12:
        average_grade = grades_counter / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break


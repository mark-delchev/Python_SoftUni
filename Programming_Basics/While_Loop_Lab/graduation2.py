name = input()
years_counter = 0
failed_grades = 0
sum_grades = 0

while True:
    grades = float(input())
    years_counter += 1
    sum_grades += grades
    if grades < 4.00:
        sum_grades -= grades
        failed_grades += 1
        years_counter -= 1
        if failed_grades == 2:
            print(f'{name} has been excluded at {years_counter + 1} grade')
            break
    if years_counter == 12:
        average_grade = sum_grades / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break


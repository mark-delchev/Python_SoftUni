number_of_bad_grades = int(input())
bad_grades = 0
grades_sum = 0
grades_num = 0
last_task = ''
while bad_grades < number_of_bad_grades:
    task_name = input()
    if task_name == 'Enough':
        average_grade = grades_sum / grades_num
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {grades_num}')
        print(f'Last problem: {last_task}')
        break
    last_task = task_name
    grade = int(input())
    grades_sum += grade
    grades_num += 1
    if grade <= 4.00:
        bad_grades += 1
    if bad_grades == number_of_bad_grades:
        print(f'You need a break, {number_of_bad_grades} poor grades.')
        break



number_of_judges = int(input())
total_grade_sum = 0
presentation_grade_sum = 0
presentation_num = 0

while True:
    presentation_name = input()
    presentation_grade_sum = 0
    if presentation_name == "Finish":
        break
    else:
        presentation_num += 1
    for i in range(1, number_of_judges + 1):
        grade = float(input())
        total_grade_sum += grade
        presentation_grade_sum += grade
    presentation_grade = presentation_grade_sum / number_of_judges
    print(f"{presentation_name} - {presentation_grade:.2f}.")
total_grade = total_grade_sum / (presentation_num * number_of_judges)
print(f"Student's final assessment is {total_grade:.2f}.")

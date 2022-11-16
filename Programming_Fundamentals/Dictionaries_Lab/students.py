
student_information = input()
students = {}

while not students.get(student_information):
    student_information = student_information.split(":")
    key = student_information[0]
    value = student_information[1]
    course = student_information[-1]

    if course not in students:
        students[course] = {}
    students[course][key] = value
    student_information = input()
    student_information = student_information.replace("_", " ")

for key, value in students[student_information].items():
    print(f"{key} - {value}")

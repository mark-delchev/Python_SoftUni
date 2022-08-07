number_of_groups = int(input())

listUnder6 = 0
listUnder13 = 0
listUnder26 = 0
listUnder41 = 0
listOver40 = 0

for i in range(1, number_of_groups + 1):
    number_of_people = int(input())
    if number_of_people <= 5:
        listUnder6 += number_of_people
    if 6 <= number_of_people <= 12:
        listUnder13 += number_of_people
    if 13 <= number_of_people <= 25:
        listUnder26 += number_of_people
    if 26 <= number_of_people <= 40:
        listUnder41 += number_of_people
    if number_of_people > 40:
        listOver40 += number_of_people
total_people = listUnder6 + listUnder13 + listUnder26 + listUnder41 + listOver40

print(f'{(listUnder6 / total_people) * 100:.2f}%')
print(f'{(listUnder13 / total_people) * 100:.2f}%')
print(f'{(listUnder26 / total_people) * 100:.2f}%')
print(f'{(listUnder41 / total_people) * 100:.2f}%')
print(f'{(listOver40 / total_people) * 100:.2f}%')

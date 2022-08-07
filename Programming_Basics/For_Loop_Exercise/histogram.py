n = int(input())
listUnder200 = []
listUnder400 = []
listUnder600 = []
listUnder800 = []
listOver800 = []

for i in range(0, n):
    num = int(input())
    if num < 200:
        listUnder200.append(num)
    if 200 <= num < 400:
        listUnder400.append(num)
    if 400 <= num < 600:
        listUnder600.append(num)
    if 600 <= num < 800:
        listUnder800.append(num)
    if num >= 800:
        listOver800.append(num)

total_numbers = n
print(f'{(len(listUnder200) / total_numbers) * 100:.2f}%')
print(f'{(len(listUnder400) / total_numbers) * 100:.2f}%')
print(f'{(len(listUnder600) / total_numbers) * 100:.2f}%')
print(f'{(len(listUnder800) / total_numbers) * 100:.2f}%')
print(f'{(len(listOver800) / total_numbers) * 100:.2f}%')









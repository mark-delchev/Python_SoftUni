n = int(input())

all_nums = []
odd_nums = []
even_nums = []
negative_nums = []
positive_nums = []

for i in range(n):
    num = int(input())
    all_nums.append(num)
    if num % 2 == 0:
        even_nums.append(num)
    elif num % 2 != 0:
        odd_nums.append(num)
    if num >= 0:
        positive_nums.append(num)
    elif num < 0:
        negative_nums.append(num)

command = input()
if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "positive":
    print(positive_nums)
elif command == "negative":
    print(negative_nums)




import itertools

factor = int(input())
lst_length = int(input())
nums = []

for i in itertools.count(1):
    if len(nums) == lst_length:
        break
    if i % factor == 0:
        nums.append(i)

print(nums)



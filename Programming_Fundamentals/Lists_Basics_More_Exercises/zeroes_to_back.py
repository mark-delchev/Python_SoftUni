nums = input().split(", ")
nums_int = []
for i in nums:
    nums_int.append(int(i))
for i in range(len(nums)):
    if nums_int[i] == 0:
        nums_int.remove(0)
        nums_int.append(0)


print(nums_int)
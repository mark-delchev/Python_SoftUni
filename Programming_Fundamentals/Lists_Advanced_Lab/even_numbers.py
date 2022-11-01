nums = input().split(", ")
nums_int = [int(i) for i in nums]
positions = []
for i in range(len(nums_int)):
    num = nums_int[i]
    if num % 2 == 0:
        positions.append(i)
print(positions)
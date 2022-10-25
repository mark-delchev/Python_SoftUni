def sequence(n):
    nums = []
    for i in range(n):
        if len(nums) == 2:
            a = nums[-1] + nums[-2]  
        elif len(nums) > 2:
            a = nums[-1] + nums[-2] + nums[-3]
        else:
            a = 1
        nums.append(a)
        print(a, end=" ")

p = int(input())
sequence(p)

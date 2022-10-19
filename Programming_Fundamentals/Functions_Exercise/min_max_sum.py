def min_max_sum(str):
    lst = [int(i) for i in str.split(" ")]
    min_lst = min(lst)
    max_lst = max(lst)
    sum_lst = sum(lst)
    print(f"The minimum number is {min_lst}")
    print(f"The maximum number is {max_lst}")
    print(f"The sum number is: {sum_lst}")

nums = input()
min_max_sum(nums)
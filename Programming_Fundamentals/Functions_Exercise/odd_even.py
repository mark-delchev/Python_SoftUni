def sums(num):
    num_str = str(num)
    even_nums = []
    odd_nums = []
    for i in num_str:
        if int(i) % 2 == 0:
            even_nums.append(int(i))
        else:
            odd_nums.append(int(i))
    odd_sum = sum(odd_nums)
    even_sum = sum(even_nums)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

n = int(input())
sums(n)

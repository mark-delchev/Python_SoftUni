n = int(input())
sum_n = 0
while sum_n < n:
    current_n = int(input())
    sum_n += current_n
    if sum_n == n:
        break
print(sum_n)

def perfect_num(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")    

n = int(input())
perfect_num(n)
    


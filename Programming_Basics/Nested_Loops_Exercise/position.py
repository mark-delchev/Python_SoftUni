num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    string = str(i)
    sum_even = int(string[0]) + int(string[2]) + int(string[4])
    sum_odd = int(string[1]) + int(string[3]) + int(string[5])
    if sum_even == sum_odd:
        print(i, end=" ")


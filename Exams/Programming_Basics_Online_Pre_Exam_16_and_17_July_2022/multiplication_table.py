num = int(input())
str_num = str(num)
num1 = int(str_num[2])
num2 = int(str_num[1])
num3 = int(str_num[0])
for i in range(1, num1 + 1):
    for j in range(1, num2 + 1):
        for k in range(1, num3 + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")

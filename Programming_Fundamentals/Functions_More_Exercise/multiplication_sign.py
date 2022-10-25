def sign(n1, n2, n3):
    neg_nums = 0
    if n1 < 0:
        neg_nums += 1
    if n2 < 0:
        neg_nums += 1
    if n3 < 0:
        neg_nums += 1
    if n1 == 0 or n2 == 0 or n3 == 0:
        print("zero") 
    elif neg_nums % 2 == 0:
        print("positive")
    else:
        print("negative")

num1 = int(input())
num2 = int(input())
num3 = int(input())
sign(num1, num2, num3)

    
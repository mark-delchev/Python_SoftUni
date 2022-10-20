def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1)

def division(n1, n2):
    final_result = fact(n1) / fact(n2)
    print(f"{final_result:.2f}")

num1 = int(input())
num2 = int(input())

division(num1, num2)
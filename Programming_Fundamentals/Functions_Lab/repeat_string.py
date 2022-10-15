def repeat(string, num):
    x = lambda string, num: string * num
    return x(string, num)

s = input()
n = int(input())
print(repeat(s, n))
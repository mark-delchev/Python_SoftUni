deposit = float(input())
srok = int(input())
lihva = float(input()) / 100
sum = deposit + srok * ((deposit * lihva) / 12)
print(sum)
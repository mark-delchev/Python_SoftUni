n = int(input())
capacity = 255
liters_poured = 0
for i in range(n):
    liters_add = int(input()) 
    liters_poured += liters_add
    if liters_poured > capacity:
        liters_poured -= liters_add
        print("Insufficient capacity!")
print(liters_poured)


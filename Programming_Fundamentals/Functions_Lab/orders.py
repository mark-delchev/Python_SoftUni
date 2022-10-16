
product = input()
quantity = int(input())

if product == "coffee":
    price = 1.50
elif product == "water":
    price = 1.00
elif product == "coke":
    pice = 1.40
elif product == "snacks":
    price = 2.00
final_price = price * quantity
print(f"{final_price:.2f}")


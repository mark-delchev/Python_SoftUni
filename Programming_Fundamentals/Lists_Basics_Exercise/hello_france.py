clothes = input().split("|")
budget = float(input())
interim_budget = 0
profit = 0
sold_clothes = []
clothes_type = [i.split("->")[0] for i in clothes]
clothes_price = [float(i.split("->")[1]) for i in clothes]

for i in range(len(clothes_type)):
    new_price = 0
    price = float(clothes_price[i])
    type = clothes_type[i]

    if type == "Clothes" and price > 50:
        continue
    elif type == "Shoes" and price > 35:
        continue
    elif type == "Accessories" and price > 20.5:
        continue
    if budget >= price:
        budget -= price
        new_price += (price * 1.4)
        interim_budget += (price * 1.4)
        profit += new_price - price
        sold_clothes.append((f"{new_price:.2f}"))

sold_clothes_final = " ".join(str(i) for i in sold_clothes)
print(sold_clothes_final)
print(f"Profit: {profit:.2f}")
total_budget = interim_budget + budget
if total_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")




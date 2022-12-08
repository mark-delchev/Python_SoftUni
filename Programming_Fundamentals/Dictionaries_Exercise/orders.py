products = {}
while True:
    info = input().split(" ")
    name = info[0]
    if name == "buy":
        break
    else:
        price = info[1]
        quantity = info[2]
        final_price = float(price) * float(quantity)
        if name not in products.keys():
            products[name] = final_price
        else:
            products[name] += final_price

for k, v in products.items():
    print(f"{k} -> {v:.2f}")


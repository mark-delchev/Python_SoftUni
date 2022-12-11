
products = {}
products_last_price = {}
products_last_quantity = {}
while True:
    info = input().split(" ")
    name = info[0]
    if name == "buy":
        break
    else:
        price = info[1]
        quantity = info[2]
        if products.get(name, float(price)) != float(price):
            final_price = (float(price) * (float(quantity) + products_last_quantity.get(name, 0))) \
                          - products.get(name, 0)
        else:
            final_price = float(price) * float(quantity)

        products_last_price[name] = float(price)
        if name in products_last_quantity.keys():
            products_last_quantity[name] += float(quantity)
        else:
            products_last_quantity[name] = float(quantity)

        if name not in products.keys():
            products[name] = final_price
        else:
            products[name] += final_price

for k, v in products.items():
    print(f"{k} -> {v:.2f}")


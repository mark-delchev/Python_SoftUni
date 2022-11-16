
products = {}
while True:
    command = input()
    if command == "statistics":
        break
    product = command.split(": ")
    key = product[0]
    value = int(product[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value


print(f"Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

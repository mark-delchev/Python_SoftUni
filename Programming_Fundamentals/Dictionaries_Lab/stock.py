elements = input().split(" ")
stock = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)

search_products = input().split(" ")
for i in search_products:
    if i in stock:
        print(f"We have {stock[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")

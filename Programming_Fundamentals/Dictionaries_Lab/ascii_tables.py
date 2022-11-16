elements = {}
chars = [i for i in input().split(", ")]

for i in chars:
    key = i
    value = ord(i)
    elements[key] = int(value)

print(elements)
chars = input().split(" ")
count = {}

for i in chars:
    for k in i:
        if k in count:
            count[k] += 1
        else:
            count[k] = 1

for (key, value) in count.items():
    print(f"{key} -> {value}")

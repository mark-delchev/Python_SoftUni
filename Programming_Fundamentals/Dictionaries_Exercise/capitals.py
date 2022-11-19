countries = input().split(", ")
capitals = input().split(", ")
dic = dict(zip(capitals, countries))

for key, value in dic.items():
    print(f"{value} -> {key}")



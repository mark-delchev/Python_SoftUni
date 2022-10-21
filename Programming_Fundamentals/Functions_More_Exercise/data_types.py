def types(type, data):
    if type == "int":
        output = int(data) * 2
        print(output)
    elif type == "real":
        output = float(data) * 1.5
        print(f"{output:.2f}")
    else:
        print(f"${data}$")

t = input()
d = input()
types(t, d)


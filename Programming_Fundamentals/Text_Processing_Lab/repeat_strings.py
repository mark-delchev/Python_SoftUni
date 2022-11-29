strings = input().split(" ")

all_strings = ""
for i in strings:
    n = len(i)
    all_strings += i*n

print(f"{all_strings}")

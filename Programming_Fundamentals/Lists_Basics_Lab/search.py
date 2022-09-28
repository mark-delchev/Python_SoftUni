

n = int(input())
keyword = input()
all_strings = []
substrings = []

for i in range(n):
    phrase = input()
    all_strings.append(phrase)
    if keyword in phrase:
        substrings.append(phrase)

print(all_strings)
print(substrings)


elements = {}
word = [i for i in input().split(" ")]
odd_occurrences = []

for i in word:
    if i.lower() in elements:
        elements[i.lower()] += 1
    else:
        elements[i.lower()] = 1

for i in elements.keys():
    if elements.get(i) % 2 != 0 and i.lower() not in odd_occurrences:
        odd_occurrences.append(i.lower())

print(" ".join(odd_occurrences))
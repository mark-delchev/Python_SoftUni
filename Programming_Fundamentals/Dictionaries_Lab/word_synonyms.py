n = int(input())
pairs = {}

for i in range(0, 2 * n):
    word = input()
    if i % 2 == 0:
        previous_word = word
        try:
            test = pairs[word]
        except KeyError:
            pairs[word] = None

    else:
        if pairs[previous_word] is None:
            pairs.update({previous_word: [word]})
        else:
            pairs[previous_word].append(word)

for keys, value in pairs.items():
    print(f"{keys} - {', '.join(value)}")

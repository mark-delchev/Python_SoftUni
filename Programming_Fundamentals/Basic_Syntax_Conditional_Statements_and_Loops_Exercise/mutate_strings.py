word1 = input()
word2 = input()
word1_loop = word1
length = len(word1)
for i in range(len(word1)):
    word1_loop = word1_loop[:i] + word2[i] + word1_loop[i + 1:]
    if word1[i] == word2[i]:
        continue
    print(word1_loop)
    if word1_loop == word2:
        break
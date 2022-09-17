word1 = input()
word2 = input()
length = len(word1)
for i in range(len(word1)):
    word1 = word1[:i] + word2[i] + word1[i + 1:]
    if word1[:i] == word2[i]:
        continue
    print(word1)
    if word1 == word2:
        break
    
    
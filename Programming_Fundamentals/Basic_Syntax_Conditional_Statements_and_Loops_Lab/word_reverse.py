word = input()
length = len(word) - 1
reversed_word = ""
for i in range(length, -1, -1):
    reversed_word += word[i]
print(reversed_word)
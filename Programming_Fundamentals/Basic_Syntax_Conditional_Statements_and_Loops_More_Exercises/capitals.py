from curses.ascii import isupper


word = input()
word_list = []
capital_list = []

for c in word:
    word_list.append(c)

for i in range(len(word_list)):
    letter = word_list[i]
    if letter.isupper():
        capital_list.append(i)

print(capital_list)
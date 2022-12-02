banned_words = input().split(", ")
text = input()

for word in banned_words:
    length = len(word)
    asterisks = "*" * length
    if word in text:
        text = text.replace(word, asterisks)
print(text)

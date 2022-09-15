strings = int(input())
for string in range(strings):
    word = input()
    for i in word:
        if i == "," or i == "." or i == "_":
            print(f"{word} is not pure!")
            break
    else:
        print(f"{word} is pure.")
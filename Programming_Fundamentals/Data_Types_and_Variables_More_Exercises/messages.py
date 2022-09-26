key = int(input())
n = int(input())

original_letters = []
key_letters = []
final_letters = []

for i in range(n):
    letter = input()
    letter_code = ord(letter)
    original_letters.append(letter_code)

for i in original_letters:
    key_letter = i + key
    key_letters.append(key_letter)

for i in key_letters:
    final_letter = chr(i)
    final_letters.append(final_letter)

for i in final_letters:
    print(f"{i}", end="")

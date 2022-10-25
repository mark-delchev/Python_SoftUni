text = input()
lst1 = [i for i in text]
vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
lst2 = [k for k in lst1 if k not in vowels]
print("".join(lst2))
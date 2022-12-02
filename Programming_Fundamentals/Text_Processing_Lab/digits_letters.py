text = input()
nums = ""
letters = ""
other = ""

for char in text:
    if 48 <= ord(char) <= 57:
        nums += char
    elif 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        letters += char
    else:
        other += char

print(nums)
print(letters)
print(other)
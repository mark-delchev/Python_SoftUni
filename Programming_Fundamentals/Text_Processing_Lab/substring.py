substring = input()
string = input()


while True:
    if substring in string:
        string = string.replace(substring, "")
    else:
        break

print(string)

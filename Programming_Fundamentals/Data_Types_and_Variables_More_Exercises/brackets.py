import sys

n = int(input())
closing_brackets = 0
opening_brackets = 0
total_brackets = 0
last_string = ""

for i in range(n):
    string = input()
    if total_brackets % 2 != 0:
        if last_string == ")" and string == "(":
            closing_brackets = -(sys.maxsize)
    if string == last_string:
        closing_brackets = -(sys.maxsize)
    if string == "(":
        last_string = string
        opening_brackets += 1
        total_brackets += 1
    elif string == ")":
        last_string = string
        closing_brackets += 1
        total_brackets += 1

if closing_brackets == opening_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")




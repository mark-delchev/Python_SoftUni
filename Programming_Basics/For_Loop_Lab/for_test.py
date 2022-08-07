#for numbers in range(1, 101):
    #print(numbers)
"""
n = int(input())
for number in range(1, n + 1, 3):
    print(number)
"""
"""
n = int(input())
number = 1
for i in range(0, n + 1, 2):
    print(number)
    number = number * 2 * 2
"""
"""
n = int(input())
for i in range (n, 0, -1):
    print(i)"""
"""
n = str(input())
for char in n:
    print(char)
"""

text = str(input())
sum = 0
for i in range(0, len(text)):
    if text[i] == 'a':
        sum += 1
    if text[i] == 'e':
        sum += 2
    if text[i] == 'i':
        sum += 3
    if text[i] == 'o':
        sum += 4
    if text[i] == 'u':
        sum += 5
print(sum)


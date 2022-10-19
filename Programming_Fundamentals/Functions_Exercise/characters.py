def asciii(char1, char2):
    for i in range(ord(char1) + 1, ord(char2)):
        print(chr(i), end=" ")

c1 = input()
c2 = input()
asciii(c1, c2)

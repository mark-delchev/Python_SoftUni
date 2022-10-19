def palindrome(str):
    lst = str.split(", ")
    for i in lst:
        print(i[::-1] == i)

num = input()
palindrome(num)
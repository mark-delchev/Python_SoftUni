messages = int(input())
for message in range(messages):
    num = int(input())
    if num == 88:
        print("Hello")
    if num == 86:
        print("How are you?")
    if num != 86 and num < 88:
        print("GREAT!")
    if num > 88:
        print("Bye.")
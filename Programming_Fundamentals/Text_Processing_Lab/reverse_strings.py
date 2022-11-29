
while True:
    text = input()
    if text == "end":
        break
    text_reversed = ""
    for ch in reversed(text):
        text_reversed += ch
    print(f"{text} = {text_reversed}")


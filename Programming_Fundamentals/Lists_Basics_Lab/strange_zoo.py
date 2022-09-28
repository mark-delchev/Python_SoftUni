tail = input()
body = input()
head = input()

meerkats = [tail, body, head]

meerkats[0], meerkats[2] = meerkats[2], meerkats[0]
print(meerkats)
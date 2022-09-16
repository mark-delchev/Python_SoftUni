from curses.ascii import isupper


coffee_needed = 0
while True:
    event = input()
    if event == "END":
        break
    if event.lower() == "cat" or event.lower() == "coding" or event.lower() == "dog" or event.lower() == "movie":
        if event.isupper():
            coffee_needed += 2
        else:
            coffee_needed += 1
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)

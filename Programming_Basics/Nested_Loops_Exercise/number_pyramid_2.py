number = int(input())
IsPrinted = False
counter = 1
for row in range(1, number + 1):
    for column in range(1, row):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            IsPrinted = True
            break
    if IsPrinted:
        break
    print()

while True:
    word = input()
    if word == "End":
        break
    if word != "SoftUni":
        for i in word:
            for b in range(2):
                print(i, end= "")
        print()
            


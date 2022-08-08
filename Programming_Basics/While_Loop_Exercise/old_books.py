searched_book = input()
current_book = input()
books_searched = 0
while current_book != 'No More Books':
    if current_book == searched_book:
        print(f"You checked {books_searched} books and found it.")
        break
    current_book = input()
    books_searched += 1
    if current_book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {books_searched} books.")




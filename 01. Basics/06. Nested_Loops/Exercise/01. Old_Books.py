searched_book = str(input())

book_counter = 0
searcher = ""

while searcher != "No More Books":
    searcher = str(input())
    book_counter += 1
    if searcher == searched_book:
        book_counter -= 1
        print(f"You checked {book_counter} books and found it.")
        break

if searcher == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {book_counter - 1} books.")

books = []

while True:
    print("\n1. Добави книга")
    print("2. Покажи книги")
    print("3. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        title = input("Въведи име на книга: ")
        books.append(title)
        print("Книгата е добавена.")

    elif choice == "2":
        print("Списък с книги:")
        for book in books:
            print(book)

    elif choice == "3":
        break

    else:
        print("Невалиден избор.")
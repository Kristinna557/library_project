from models import Library

library = Library()

while True:
    print("\n1. Добави книга")
    print("2. Покажи книги")
    print("3. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        title = input("Въведи име на книга: ")
        library.add_book(title)
        print("Книгата е добавена.")

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        break

    else:
        print("Невалиден избор.")
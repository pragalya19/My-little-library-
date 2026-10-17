books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author
    }

    books.append(book)
    print("Book added successfully!")

def view_books():
    if len(books) == 0:
        print("Your library is empty!")
    else:
        print("\n📚 MY LITTLE LIBRARY")

        for book in books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("-------------------")

while True:
    print("\n📚 MY LITTLE LIBRARY")
    print("1. Add a book")
    print("2. View my books")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        print("Happy reading! Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

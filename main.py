from books import addBook, viewBook, issueBook, returnBook, searchBook, deleteBook
def menu():
    while True:
        print("\n===Welcome To Library Management System===")
        print("\nChoose Your Option--->")
        print("---> 1. Add Book")
        print("---> 2. View Book")
        print("---> 3. Issue Book")
        print("---> 4. Return Book")
        print("---> 5. Search Book")
        print("---> 6. Delete Book")
        print("---> 7. Exit The Menu")

        ch = input("Enter Your Choice:")
        print()
        if ch == "1":
            addBook()
        elif ch == "2":
            viewBook()
        elif ch == "3":
            issueBook()
        elif ch == "4":
            returnBook()
        elif ch == "5":
            searchBook()
        elif ch == "6":
            deleteBook()
        elif ch == "7":
            print("\nExiting The Menu...")
            break
        else:
            print("\nInvalid Choice")

menu()

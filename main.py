from book import addBook, viewBook, issueBook, returnBook
def menu():
    while True:
        print("\n===Welcome To Library Management System===")
        print("\nChoose Your Option--->")
        print("---> 1. Add Book")
        print("---> 2. View Book")
        print("---> 3. Issue Book")
        print("---> 4. Return Book")
        print("---> 5. Search Book")
        print("---> 6. Exit The Menu")

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
            print("\nExiting The Menu...")
            break
        else:
            print("\nInvalid Choice")

menu()
library = []

def addBook():
    bid = input("Enter Book ID:").strip()
    for book in library:
        if book["id"] == bid:
            print("This Book ID already used, Try Different ID")
            return
    ttl = input("Enter Book Title:")
    auth = input("Enter Author Name:")
    gen = input("Enter Genre:")
    lan = input("Enter Language:")

    book = { "id":bid, "ttl":ttl, "auth":auth, "gen":gen, "lan":lan, "status": False }

    library.append(book)

    print("Book Added Successfully!")
    print()

def viewBook():
    if not library:
        print("Sorry library is empty")

    print("\n---List Of Books In Library---")
    for book in library:
        status = "Issued" if book["status"] else "Available"
        print(f' Book ID = {book["id"]} | Title = {book["ttl"]} | Author = {book["auth"]} | Genre = {book["gen"]} | Language = {book["lan"]} | Status = {status}')
    print()

def issueBook():
    bid = input("Enter Book ID:")
    for book in library:
        if book["id"] == bid:
            if not book["status"]:
                book["status"] = True
                print("Book Issued Sucessfully")
            else:
                print("Book Already Issued")
            return

    print("No Records Found")
    print()

def returnBook():
    bid = input("Enter Book ID:")
    for book in library:
        if book["id"] == bid:
            if book["status"]:
                book["status"] = False
                print("Book Returned Sucessfully")
            else:
                print("This Book Was Not Issued")
            return
    print("No Records Found")
    print()

def menu():
    while True:
        print("\n===Welcome To Library Management System===")
        print("\nChoose Your Option--->")
        print("---> 1. Add Book")
        print("---> 2. View Book")
        print("---> 3. Issue Book")
        print("---> 4. Return Book")
        print("---> 5. Exit The Menu")

        ch = input("Enter Your Choice:")
        if ch == "1":
            addBook()
        elif ch == "2":
            viewBook()
        elif ch == "3":
            issueBook()
        elif ch == "4":
            returnBook()
        elif ch == "5":
            print("Exiting The Menu...")
            break
        else:
            print("Invalid Choice")

menu()


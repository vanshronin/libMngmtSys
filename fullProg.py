library = []

def addBook():
    bid  = input("Enter Book ID:").strip()
    for book in library:
        if book["id"] == bid:
            print("\nID already exist, Try New ID")
            return
    ttl = input("Enter Book Title:")
    auth = input("Enter Author Name:")
    status = False

    book = {"id":bid,"ttl":ttl,"auth":auth,"status":status}
    library.append(book)

    print("\nBook Added Successfully")

def viewBook():
    if not library:
        print("\nLibrary Empty")
        return
    print("\n---Books In Library---")
    print()
    for book in library:
        status = "Issued" if book["status"] else "Avaiable"
        print(f"Book ID = {book["id"]} | Book Title = {book["ttl"]} | Author = {book["auth"]} | Status = {status}")
        print()

def issueBook():
    bid = input("\nEnter Book ID:").strip()
    for book in library:
        if book["id"]==bid:
            if book["status"]:
                print("\nBook Already Issued")
                return
            book["status"] = True
            print("\nBook Issued Successfully")
            return

    print("\nNo Book Records")


def returnBook():
    bid = input("\nEnter Book ID:")
    for book in library:
        if book["id"] == bid:
            if not book["status"]:
                print("\nBook Was Not Issued")
                return
            book["status"] = False
            print("\nBook Returned Successfully")
            return
    print("\nNo Records Found")

def searchBook():
    key = input("Enter Book ID or Title:").strip().lower()
    if not library:
        print("\nNo Record Found")
        return
    for book in library:
        if book["id"]==key or book["ttl"].lower() == key:
            print("\nSearch Results:")
            status = "Issued" if book["status"] else "Avaiable"
            print(f"\nBook ID = {book["id"]} | Book Title = {book["ttl"]} | Author = {book["auth"]} | Status = {status}")

def deleteBook():
    bid = input("Enter Book ID:")

    for book in library:
        if book["id"] == bid:
            if book["status"]:
                print("\nBook Is Issued, Return Book")
                return
            library.remove(book)
            print("\nBook Deleted Successfully")
            return
    print("\nNo Records Found")

def menu():
    while True:
        print("--------------------------------------------")
        print("===Welcome To Library Management System===")
        print("\n Choose Operation--->")
        print("---> 1. Add Book")
        print("---> 2. View Book")
        print("---> 3. Issue Book")
        print("---> 4. Return Book")
        print("---> 5. Search Book")
        print("---> 6. Delete Book")
        print("---> 7. Exit LMS")

        ch = input("\nChoose Your Option:")
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
            print("\nExiting The System")
        else:
            print("Invalid Choice")

menu()

















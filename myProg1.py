import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5126",
    database="libMngmtSys"
)

cursor = conn.cursor()
cursor.execute("INSERT INTO books(ID,Title,Author,Genre,Language,Status) VALUES(%s,%s,%s,%s,%s,%s)",
               ("101", "Demo Book", "Test Author", "Fiction", "English", False)
               )

conn.commit()

print("Book inserted successfully")

library = []

def addBook():
    bid = input("Enter Book ID:").strip()
    for book in library:
        if book["id"] == bid:
            print("This Book ID already exists, Try Different ID X(")
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
        print("Sorry library is empty :(")

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
                print("\nBook Issued Successfully!!")
            else:
                print("\nBook Already Issued :(")
            return

    print("\nNo Records Found X(")
    print()

def returnBook():
    bid = input("Enter Book ID:")
    for book in library:
        if book["id"] == bid:
            if book["status"]:
                book["status"] = False
                print("\nBook Returned Successfully!!")
            else:
                print("\nThis Book Was Not Issued :(")
            return
    print("\nNo Records Found X(")
    print()

def searchBook():
    if not library:
        print("No Books in Library")
        return
    key = input("Enter Book ID or Book Title:").strip().lower()
    found = False
    for book in library:
        if book["id"] == key or key in book["ttl"].lower():
            if not found:
                print("\nBooks Found--->")
                found = True
            status = "Issued" if book["status"] else "Available"
            print(f'\nBook ID = {book["id"]} | Title = {book["ttl"]} | Author = {book["auth"]} | Genre = {book["gen"]} | Language = {book["lan"]} | Status = {status}')
    if not found:
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

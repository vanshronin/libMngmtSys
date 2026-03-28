from db import conn, cursor

library = []

def addBook():
    bid = input("Enter Book ID: ").strip()

    cursor.execute("SELECT * FROM books WHERE ID = %s", (bid,))
    result = cursor.fetchone()

    if result:
        print("This Book ID already exists, Try Different ID X(")
        return

    ttl = input("Enter Book Title: ")
    auth = input("Enter Author Name: ")
    gen = input("Enter Genre: ")
    lan = input("Enter Language: ")

    cursor.execute(
        "INSERT INTO books(ID, Title, Author, Genre, Language, Status) VALUES(%s, %s, %s, %s, %s, %s)",
        (bid, ttl, auth, gen, lan, False)
    )

    conn.commit()

    print("Book Added Successfully!\n")


# SQL integration pending




def viewBook():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()

    if not records:
        print("Sorry library is empty :(")
        return

    print("\n---List Of Books In Library---")

    for book in records:
        status = "Issued" if book[5] else "Available"

        print(f' Book ID = {book[0]} | Title = {book[1]} | Author = {book[2]} | Genre = {book[3]} | Language = {book[4]} | Status = {status}')

    print()

viewBook()

'''def issueBook():
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
    print()'''

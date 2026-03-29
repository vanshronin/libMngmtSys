from db import conn, cursor


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
        (bid, ttl, auth, gen, lan, False))

    conn.commit()

    print("Book Added Successfully!\n")


def viewBook():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()

    if not records:
        print("Sorry library is empty :(")
        return

    print("\n---List Of Books In Library---")

    for books in records:
        status = "Issued" if books[5] else "Available"

        print(f' Book ID = {books[0]} | Title = {books[1]} | Author = {books[2]} | Genre = {books[3]} | Language = {books[4]} | Status = {status}')

    print()


def issueBook():
    bid = input("Enter Book ID:").strip()
    cursor.execute("SELECT Status FROM books WHERE ID = %s",(bid,))
    result = cursor.fetchone()

    if not result:
        print("\n No Book Records Found X(")
        return
    if result[0] == 1:
        print("\n Book Already Issued :(")
        return

    cursor.execute("UPDATE books SET Status = %s WHERE ID = %s",(1,bid))
    conn.commit()
    print("\nBook Issued Successfully :)")



def returnBook():
    bid = input("Enter Book ID:").strip()
    cursor.execute("SELECT Status FROM books WHERE ID = %s",(bid,))
    result = cursor.fetchone()
    if not result:
       print("No Record Found X(")
       return
    if result[0] == 0:
        print("This Book Was Not Issued :(")
        return

    cursor.execute("UPDATE books SET Status = %s WHERE ID = %s",(0,bid))
    conn.commit()
    print("Book Returned Successfully :)")


def searchBook():
    key = input("\nEnter Book ID, Title, Genre:").strip().lower()

    cursor.execute("SELECT * FROM books WHERE ID = %s OR LOWER(Title) LIKE %s OR LOWER(Genre) LIKE %s",(key,f"%{key}%",f"%{key}%"))

    result = cursor.fetchall()

    if not result:
        print("No Record Found :(")
        return

    print("\n Books Matching Your Search:")

    for books in result:
        status = "Issued" if books[5] else "Available"

        print(f' Book ID = {books[0]} | Title = {books[1]} | Author = {books[2]} | Genre = {books[3]} | Language = {books[4]} | Status = {status}')

issueBook()

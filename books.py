from db import conn,cursor

def addBook():
    bid = input("Enter Book ID:")
    cursor.execute("SELECT * FROM books WHERE ID = %s", (bid,))
    result = cursor.fetchone()

    if result:
        print("This ID already exist, Try New ID !!")
        return
    ttl = input("Enter Book Title:\n")
    auth = input("Enter Author Name:\n")
    gen = input("Enter Book Genre:\n")
    lan = input("Enter Book Language:\n")

    cursor.execute("INSERT INTO books(ID,Title,Author,Genre,Language,Status) VALUES(%s,%s,%s,%s,%s,%s)",(bid,ttl,auth,gen,lan,False))
    conn.commit()

    print("Book Added Successfully :)")
print()

def viewBook():
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    if not results:
        print("Library Empty")
        return
    print("---List Of Books In Library---")
    for books in results:
        status = "Issued" if books["Status"] else "Available"
        print(f'Book ID :{books["ID"]} | Book Title : {books["Title"]} | Author : {books["Author"]} | Genre : {books["Genre"]} | Language : {books["Language"]} | Status : {status}')
print()

def issueBook():
    bid = input("Enter Book ID:")
    cursor.execute("SELECT Status FROM books WHERE ID = %s",(bid,))
    result = cursor.fetchone()

    if not result:
        print("\nNo Records Found :(")
        return

    if result["Status"]:
        print("\nBook Already Issued !!")
        return

    cursor.execute("UPDATE books SET Status = %s WHERE ID = %s",(1,bid))
    conn.commit()

    print("\nBook Issued Successfully :)")

def returnBook():
    bid = input("Enter Book ID:")
    cursor.execute("SELECT Status FROM books WHERE ID = %s",(bid,))
    result = cursor.fetchone()
    if not result:
        print("\nNo Records Found :(")
        return
    if not result["Status"]:
        print("\nThis Book Was Not Issued !!")
        return
    cursor.execute("UPDATE books SET Status = %s WHERE ID = %s",(0,bid,))
    print("\nBook Returned Successfully :)")
    conn.commit()
print()

def searchBook():
    key = input("Enter Book ID, Title or Genre:").strip().lower()
    cursor.execute("SELECT * FROM books WHERE ID = %s OR LOWER(Title) LIKE %s OR LOWER(Genre) LIKE %s",(key,f"%{key}%",f"%{key}%"))
    results = cursor.fetchall()
    if not results:
        print("\nNo Such Book In Library :(")
        return
    print("\n---Matching Results---")
    for books in results:
        status = "Issued" if books["Status"] else "Available"
        print(f'Book ID :{books["ID"]} | Book Title : {books["Title"]} | Author : {books["Author"]} | Genre : {books["Genre"]} | Language : {books["Language"]} | Status : {status}')
    print()

def deleteBook():
    bid = input("Enter Book ID:")
    cursor.execute("SELECT Status FROM books WHERE ID = %s",(bid,))
    result = cursor.fetchone()

    if not result:
        print("No Such Book In Library :(")
        return

    if result["Status"]:
        print("Return Book First")
        return

    cursor.execute("DELETE FROM books WHERE ID = %s",(bid,))
    conn.commit()

    print("Book Deleted Successfully :)")
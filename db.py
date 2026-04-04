import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5126",
    database="libMngmtSys"
)

cursor = conn.cursor(dictionary = True)

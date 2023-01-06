import sqlite3

conn = sqlite3.connect("customer.db")

#Create a Cursor

c = conn.cursor()

#Create a Table

c.execute("INSERT INTO customer VALUES('Tim','Smith','ramlal')")

conn.commit()

conn.close()

#NULL
#INTEGER
#REAL
#TEXT
#BLOB
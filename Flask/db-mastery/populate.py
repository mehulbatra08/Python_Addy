import sqlite3
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()
# c.execute("""
# CREATE TABLE contact_details
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT)
# """)
c.execute("""
INSERT INTO contact_details
(username) VALUES('ramlal')
""")
conn.commit()


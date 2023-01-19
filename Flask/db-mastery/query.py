import sqlite3
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()
# c.execute("""
# CREATE TABLE contact_details
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT)
# """)
c.execute("""
SELECT * FROM contact_details
""")

student_info = c.fetchall()
for student in student_info:
    print(student)
conn.commit()


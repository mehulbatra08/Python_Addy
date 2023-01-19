from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String(80),unique = True,nullable = False)
    author = db.Column(db.String(80),unique = True,nullable = False)
    rating = db.Column(db.Float,unique = True,nullable = False)

# db.create_all()


#Create a Record
new_book = Book(id = 1,title="Harry Potter",author = "JK Rowling", rating = 9.3)

db.session.add(new_book)
db.session.commit()

#Now we will see how to use CRUD Operations

#Read
# books = Book.query.all()
# print(books)

#Update 
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit() 

#Update by Primary Key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.author = "Mehul Potter"
# db.session.commit()

#Delete by Primary Key

# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()







#SQLITE TUTORIAL
# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()


# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1,'HARRY POTTER','J.K Rowling','9.3')")



# db.commit()
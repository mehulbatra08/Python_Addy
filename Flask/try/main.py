from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)

class Phonebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Phonebook {self.name}>'

@app.route('/', methods = ['POST', 'GET'])
def hello():
    allcontacts = ""
    if request.method=='POST':
        name = request.form['name']
        phone = request.form['phone']
        entry = Phonebook(name=name,phone=phone)
        db.session.add(entry)
        db.session.commit()
        allcontacts = Phonebook.query.all() 
    return render_template('index.html',allcontacts=allcontacts)

@app.route('/delete')
def delete():
    latest_contact = Phonebook.query.first()
    db.session.delete(latest_contact)
    db.session.commit()
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)
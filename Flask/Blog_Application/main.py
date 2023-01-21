from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class myblog(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(1000),nullable = False)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods = ['POST', 'GET'])
def blog():
    allcontacts = ""
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        myBlog = myblog(title=title,desc=desc)
        db.session.add(myBlog)
        db.session.commit()
        allcontacts = myblog.query.all()
        
    return render_template('admin.html',allcontacts=allcontacts)

@app.route('/posts',methods = ['POST', 'GET'])
def posts():
    
    allcontacts = myblog.query.all()
    return render_template('posts.html',allcontacts=allcontacts)

@app.route('/delete/<sno>', methods=['POST'])
def delete(sno):
    myBlog = myblog.query.filter_by(sno=sno).first()
    db.session.delete(myBlog)
    db.session.commit()
    return redirect('/posts')


if __name__ =='__main__':
    app.run(debug=True)
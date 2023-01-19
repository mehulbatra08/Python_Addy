from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('phonebook.db') 


@app.route('/', methods = ['POST', 'GET'])
def hello():
    example_text = query()

    return render_template('home.html',example_text=example_text)

@app.route('/add/', methods = ["GET","POST"])


def add_student():
    if request.method == ["GET"]:

        return render_template("add-student.html")
    else:
        student_details = (
            request.form["username"]
        )
        insert_student(student_details)
        return render_template("success.html")

def insert_student(student_details):
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    sql_execute_string = ("INSERT INTO contact_details(username) VALUES (?)")
    c.execute(sql_execute_string,student_details)

    c.execute("""
    SELECT * FROM contact_details
    """)

    conn.commit()
    conn.close()



def query():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()

    c.execute("""
    SELECT * FROM contact_details
    """)

    student_info = c.fetchall()
    return student_info
    
    



if __name__ =='__main__':
    app.run(debug=True)




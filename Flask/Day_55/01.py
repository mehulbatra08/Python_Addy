from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello_world():
    return '<h1 style = "text-align: center"> Hello, World </h1>'\
    '<p>Hello Everyone My Name is Mehul and I want to be a Python Developer!</p>'\
    '<img src = "https://media.giphy.com/media/KizGHRfDRo3y8u6Sf2/giphy.gif" width = 200>'
@app.route("/bye")
def bye():
    return "Bye!"
@app.route("/<name>/<number>")
def greet(name,number):
    return f"Hello there {name} You are {number}!"

 
if __name__ == "__main__":
    app.run(debug = True)
bye()
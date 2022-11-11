from flask import Flask,render_template,request

app = Flask(__name__)

import random


@app.route('/')
def helloworld():
    name = request.args.get("name")
    return render_template("index.html",name=name)
    
    
if __name__ == "__main__":
    app.run(debug = True)

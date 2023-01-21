from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method=='POST':
        name = request.form['fname']
        print(name)

    return render_template('index.html',name=name)
if __name__ =='__main__':
    app.run(debug=True)
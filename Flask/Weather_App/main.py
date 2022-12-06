from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city_name')

        r = request.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={a4f9427ee49614c32dd788399753a372}')

    return render_template('index.html')
 
if __name__ =='__main__':
   app.run(debug=True)
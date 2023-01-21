from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def hello():
    final_name = ""
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        
        namesum = fname + lname
#Now I want to check true love in this string called namesum

        t = namesum.count('t')
        r = namesum.count('r')
        u = namesum.count('u')
        e = namesum.count('e')

        first_person = t + r + u + e


        l = namesum.count('l')
        o = namesum.count('o')
        v = namesum.count('v')
        e_2 = namesum.count('e')
        last_person = l + o + v + e_2
        final_name = str(first_person) + str(last_person)
    return render_template('index.html',final_name=final_name)
if __name__ =='__main__':
    app.run(debug=True)


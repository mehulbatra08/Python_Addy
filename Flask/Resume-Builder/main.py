from flask import Flask, request, render_template,url_for

 
# Flask constructor
app = Flask(__name__)
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/',methods = ["POST","GET"])
 
def form():
  
    
    return render_template("index.html")


    
@app.route('/output/', methods = ["POST","GET"])
 
def myoutput():
    myfname = request.form.get('fname')
    mylname = request.form.get('lname')
    myemail = request.form.get('my_email')
    mydesignation = request.form.get('mydesignation')
    mygender = str(request.form.get('mygender'))
    myage = request.form.get('myage')
    bday = request.form.get('bday')
    tenyop = request.form.get('tenyop')
    tennumber = request.form.get('tennumber')
    twelthnumber = request.form.get('twelthnumber')
    twelthyop = request.form.get('twelthyop')
    ugyop = request.form.get('ugyop')
    ugnumber = request.form.get('ugnumber')
    pgyop = request.form.get('pgyop')
    pgnumber = request.form.get('pgnumber')
    mysummary = request.form.get('mysummary')
    skillone = int(request.form.get('skillone'))
    finalskillone = skillone*10
    skillonename = request.form.get('skillonename')
    skilltwo = int(request.form.get('skilltwo'))
    finalskilltwo = skilltwo*10
    skilltwoname = request.form.get('skilltwoname')
    skillthree = int(request.form.get('skillthree'))
    finalskillthree = skillthree*10
    skillthreename = request.form.get('skillthreename')
    skillfour = int(request.form.get('skillfour'))
    finalskillfour = skillfour*10
    skillfourname = request.form.get('skillfourname')
    
    return render_template("output.html",myfname=myfname,mylname=mylname,myemail=myemail,mygender=mygender,myage=myage,bday=bday,tenyop=tenyop,tennumber=tennumber,twelthnumber=twelthnumber,twelthyop=twelthyop,ugyop = ugyop,ugnumber=ugnumber,pgyop=pgyop,pgnumber=pgnumber,mysummary=mysummary,finalskillone=finalskillone,skillonename=skillonename,finalskilltwo=finalskilltwo,skilltwoname=skilltwoname,finalskillthree=finalskillthree,skillthreename=skillthreename,finalskillfour=finalskillfour,skillfourname=skillfourname,mydesignation=mydesignation)
   




 
if __name__ =='__main__':
   app.run(debug=True)

# Domain 6.223.55.44
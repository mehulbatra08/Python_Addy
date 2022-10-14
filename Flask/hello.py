from asyncio.base_subprocess import WriteSubprocessPipeProto
from flask import Flask
app = Flask(__name__)

@app.route('/') #Forward Slash means the HOME PAGE of the website
def hello_world():
    return 'Hello, World!'

if __name__ == "main":
    app.run()


# export FLASK_APP=hello.py
# flask run





# Python Decorator Function
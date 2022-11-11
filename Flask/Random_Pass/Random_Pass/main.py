from flask import Flask,render_template,jsonify

import random


app = Flask(__name__)

@app.route("/")
def hello_world():

    

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        symbols = ["$", "!", "@", "&", "%", "*", "^"]

        numbers = ["1","2","3","4","5","6","7","8","9"]

        sum_letters = ""
        for i in range(4):

            r_letters = random.choice(letters)
            
            sum_letters = sum_letters + r_letters    
        # print(sum_letters)

        sum_symbols = ""
        for i in range(4):

            r_symbols = random.choice(symbols)
            
            sum_symbols = sum_symbols + r_symbols    
        # print(sum_symbols)

        sum_numbers = ""
        for i in range(4):

            r_numbers = random.choice(numbers)
            
            sum_numbers = sum_numbers + r_numbers    
        # print(sum_numbers)

        final = random.sample(sum_letters + sum_symbols + sum_numbers,12)
        final_password = "".join(final)

        print(final_password)
        return render_template("index.html",final_password=final_password)

if __name__ == "__main__":
    
    app.run(debug=True)
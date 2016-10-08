from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
import random

app.secret_key = "choi"

@app.route('/')
def Main():
    if "totesgold" not in session:
        session["totesgold"]=0
    return render_template('index.html')

@app.route('/Process_money',methods=["post"])
def results():
    choice= request.form['choice']
    var = 0
    if choice == "farm":
        var = random.randrange(10,20)
    elif choice == "cave":
        var = random.randrange(5,10)
    elif choice == "house":
        var = random.randrange(2,5)
    elif choice == "casino":
        var = random.randrange(-50,50)
    session["totesgold"]+=var
    return redirect('/')
app.run(debug=True)

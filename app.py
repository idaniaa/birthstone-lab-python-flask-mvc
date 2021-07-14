# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model



# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index') 
def index():
   
    return render_template("index.html")

@app.route('/result',methods=["GET","POST"])
def result(): 
    print(request.form["stone"])
    user_choice=request.form["stone"]
    
    stone= {
        "January":"Garnet",
        "Febuary":"Anethyst",
        "March":"Aquamarine",
        "April":"Diamond",
        "May":"Emerald",
        "June":"Pearl",
        "July":"Ruby",
        "August":"Peridot",
        "September":"Sapphire",
        "October":"Opal",
        "November":"Citrine",
        "December":"Topaz"}
    try:
        message=stone[user_choice]

    except:
        message=("error, please try another month")
        
    return render_template("results.html", message=message)
from flask import Flask, render_template, request
import datetime


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year= now.month == 1 and now.day ==1
    names=["evelynn", "kayn", "hecarim", "shyvana", "graves"]
    return render_template("hello2.html", title1=new_year, names=names)


@app.route('/more', methods=["GET","POST"])
def more():
	name=request.form.get("name")
	return render_template("index.html", name=name)


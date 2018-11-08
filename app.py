from flask import Flask, request
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def catbook_home():
    if request.method == 'GET':
        cats = get_all_cats()
        return render_template("home.html", cats=cats)
    else:
        cats = get_all_cats()
        name = request.form['name']
        pict = request.form['pict']
        create_cat(name, pict)
        return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def catbook_profile(id):
    cat = get_by_id(id)
    return render_template("cat.html", cat = cat)

@app.route('/add')
def catbook_adding():
    return render_template("add.html")

if __name__ == '__main__':
   app.run(debug = True)

from foodjiji import app, db
from flask import render_template, request, redirect, url_for
from foodjiji.models import Account, Post, Review

posts = [
    {
         'account': 'Mario Pizza',
         'item': 'Pepperoni Pizza',
         'nationality': 'Italian',
         'price': 15,
         'picture': 'pictures/pizza.jpg'
                },
     {
         'account': 'LaoGanMa',
         'item': 'Mapo Tofu',
         'nationality': 'Chinese',
         'price': 15,
                        }]

@app.route("/login", methods=['POST'])
def login():
    return render_template('login.html')

@app.route("/create_account", methods=['POST'])
def create_account():
    return render_template('create_account.html')

@app.route("/creating", methods=['POST'])
def creating():
    new_account = Account(request.form['username'], int(request.form['account_type'])) # create object
    db.session.add(new_account)    # add object
    db.session.commit()             # save
    return redirect(f"/")

@app.route("/", methods=['POST'])
def webapp():
    prediction = 1
    #return a html file
    return render_template('home.html', prediction=prediction, posts=posts)

@app.route('/', methods=['GET'])
def load():
    return render_template('home.html', prediction=None)
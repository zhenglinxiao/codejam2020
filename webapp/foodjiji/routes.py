from foodjiji import app, db
from flask import render_template, request, redirect
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

isLoggedIn = False
account = None

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/logging", methods=['POST'])
def logging():
    # check if username is valid
    user = Account.query.filter_by(username=request.form['username'], account_type=bool(int(request.form['account_type']))).first()

    if user:
        global isLoggedIn
        global account
        isLoggedIn = True
        account = request.form['username']
    return redirect(f"/")

@app.route("/create_account", methods=['GET'])
def create_account():
    return render_template('create_account.html')

@app.route("/creating", methods=['POST'])
def creating():
    new_account = Account(request.form['username'], int(request.form['account_type'])) # create object
    db.session.add(new_account)    # add object
    db.session.commit()            # save
    return redirect(f"/login")

@app.route("/", methods=['POST'])
def webapp():
    prediction = 1
    return render_template('home.html', prediction=prediction, posts=posts, account=account, isLoggedIn=isLoggedIn)

@app.route('/', methods=['GET'])
def load():
    return render_template('home.html', prediction=None, account=account, isLoggedIn=isLoggedIn)
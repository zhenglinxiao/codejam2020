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
        print('Successfully logged in.')
        return redirect(f"/")
    else:
        print("Invalid account.")
        return redirect(f"/create_account")


@app.route("/create_account", methods=['GET'])
def create_account():
    return render_template('create_account.html')
	
@app.route("/new_post", methods=['POST','GET'])
def new_post():
	return render_template('new_post.html')

@app.route("/writing_post", methods=['POST'])
def creating_post():
    delivery = False
    pickup = False
    if(request.form.get('delivery')):
        delivery = True
    if(request.form.get('pickup')):
        pickup = True
    new_post = Post(request.form['item_name'],
                    account,
                    request.form['description'],
                    request.form['price'],
                    request.form['start_date'],
                    request.form['end_date'],
                    request.form['location'],
                    delivery, pickup,
                    request.form['ingredients'],
                    request.form['img'])
    db.session.add(new_post)
    db.session.commit()
    print("Successfully created post.")
    return redirect(f"/")

@app.route("/creating", methods=['POST'])
def creating():
    user = Account.query.filter_by(username=request.form['username'], account_type=bool(int(request.form['account_type']))).first()
    if user:
        print("Account already exists.")
        redirect(f"/login")

    new_account = Account(request.form['username'], int(request.form['account_type'])) # create object
    db.session.add(new_account)    # add object
    db.session.commit()            # save
    print("Successfully created account. You may now login.")
    return redirect(f"/login")

@app.route("/", methods=['POST'])
def webapp():
    prediction = 1
    return render_template('home.html', prediction=prediction, posts=posts, account=account, isLoggedIn=isLoggedIn)

@app.route('/', methods=['GET'])
def load():
    return render_template('home.html', prediction=None, account=account, isLoggedIn=isLoggedIn)
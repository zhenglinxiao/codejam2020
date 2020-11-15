from sqlalchemy import func
from foodjiji import app, db
from flask import render_template, request, redirect
from foodjiji.models import Account, Post, Review
import numpy
from scoring_algorithm import scoring

isLoggedIn = False
account = None

def isLoggedInAsBuyer():
    global isLoggedIn
    global account
    if isLoggedIn:
        account_obj = Account.query.filter_by(username=account).first()
        return isLoggedIn and account_obj.account_type
    return False

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')


@app.route("/logging", methods=['POST'])
def logging():
    user = Account.query.filter_by(username=request.form['username'],
                                   account_type=bool(int(request.form['account_type']))).first()
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

@app.route("/logout", methods=['POST'])
def logout():
    global isLoggedIn
    if isLoggedIn:
        global account
        isLoggedIn = False
        account = None
        print("Logged out")
    return redirect(f"/")

@app.route("/create_account", methods=['GET'])
def create_account():
    return render_template('create_account.html')


@app.route("/creating", methods=['POST'])
def creating():
    user = Account.query.filter_by(username=request.form['username'],
                                   account_type=bool(int(request.form['account_type']))).first()
    if user:
        print("Account already exists.")
        redirect(f"/login")

    new_account = Account(request.form['username'], request.form['email'], int(request.form['account_type']))  # create object
    db.session.add(new_account)  # add object
    db.session.commit()  # save
    print("Successfully created account. You may now login.")
    return redirect(f"/login")


@app.route("/new_post", methods=['POST', 'GET'])
def new_post():
    return render_template('new_post.html')


@app.route("/writing_post", methods=['POST'])
def creating_post():
    delivery = False
    pickup = False
    if (request.form.get('delivery')):
        delivery = True
    if (request.form.get('pickup')):
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

@app.route("/account", methods=['GET'])
def account():
    user = request.args.get('user')
    user_obj = Account.query.filter_by(username=user).first()
    isAccountBuyer = user_obj.account_type
    posts = Post.query.filter_by(user=user)
    reviews = Review.query.filter_by(by_user=user)
    return render_template('account.html', account=user, isAccountBuyer=isAccountBuyer, posts=posts, reviews=reviews, isLoggedInAsBuyer=isLoggedInAsBuyer())

@app.route("/new_review", methods=['GET'])
def new_review():
    if isLoggedIn:
        for_user = request.args.get('user')
        posts = Post.query.filter_by(user=for_user)
        return render_template('new_review.html', for_user=for_user, posts=posts)
    return redirect(f"/")

@app.route("/writing_review", methods=['POST'])
def writing_review():
    if isLoggedInAsBuyer():
        for_user = request.args.get('user')
        item = request.form['item']
        rating = request.form['rating']
        new_review = Review(for_user,
                          account,
                          item,
                          rating,
                          request.form['review'])
        db.session.add(new_review)
        db.session.commit()
        print("Successfully left review.")

        item_post = Post.query.filter_by(user=for_user, item=item).first() # object
        ingredients = item_post.ingredients  # string

        list_ingredients = ingredients.split(',') # list of ingredients

        # remove leading and trailing spaces
        for i in range(len(list_ingredients)):
            list_ingredients[i] = list_ingredients[i].strip()

        user_obj = Account.query.filter_by(username=account).first()
        ingredients_vector = scoring.encode(list_ingredients)

        tmp = numpy.array(user_obj.preference)
        tmp += int(rating) * ingredients_vector
        user_obj.preference = tmp.tolist()
        db.session.commit()

        return redirect(f"/reviews?user={for_user}")
    return redirect(f"/")

@app.route("/reviews", methods=['GET'])
def review():
    user = request.args.get('user')
    user_obj = Account.query.filter_by(username=user).first()
    isAccountBuyer = user_obj.account_type

    if not isAccountBuyer:
        reviews = Review.query.filter_by(for_user=user)
        return render_template('reviews.html', account=user, reviews=reviews, isLoggedInAsBuyer=isLoggedInAsBuyer())

    return redirect(f"/")


@app.route("/", methods=['GET'])
def webapp():
    if isLoggedIn:
        user_obj = Account.query.filter_by(username=account).first()
        preference_vector = numpy.array(user_obj.preference)

        posts = Post.query.all()
        post_dict = dict()

        for post in posts:
            ingredients = post.ingredients
            list_ingredients = ingredients.split(',')
            for i in range(len(list_ingredients)):
                list_ingredients[i] = list_ingredients[i].strip()
            ingredients_vector = scoring.encode(list_ingredients)

            post_dict[post] = scoring.score(ingredients_vector, preference_vector)

        sorted_post = sorted(post_dict.items(), key=lambda x: x[1], reverse=True)
        posts  = list()
        for post in sorted_post:
            posts.append(post[0])
        print(posts)
    else:
        posts = Post.query.all()
    return render_template('home.html', posts=posts, account=account, isLoggedIn=isLoggedIn, isLoggedInAsBuyer=isLoggedInAsBuyer(), isSearchActive=False)

@app.route("/search", methods=['POST'])
def search():
    search = request.form['search_input']
    posts = Post.query.filter(func.lower(Post.item).like('%' + str.lower(search) + '%'),
                              func.lower(Post.description).like(('%' + str.lower(search) + '%')))
    return render_template('home.html', posts=posts, account=account, isLoggedIn=isLoggedIn, isLoggedInAsBuyer=isLoggedInAsBuyer(), isSearchActive=True, search=search)
#
# @app.route('/', methods=['GET'])
# def load():
#     return render_template('home.html', posts=Post.query.all(), account=account, isLoggedIn=isLoggedIn, isLoggedInAsBuyer=isLoggedInAsBuyer(), isSearchActive=False)

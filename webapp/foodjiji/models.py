from foodjiji import db

class User(db.Model):
    username = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    account_type = db.Column(db.Boolean, nullable=False)
    # posts = SELECT * FROM post WHERE user = username
    # reviews = SELECT * FROM review WHERE for_user = username

class Post(db.Model):
    id = db.Column(db.BIGINT, nullable=False, unique=True, primary_key=True)
    item = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(20), nullable=False) # should correspond to an user
    description = db.Column(db.String(140))
    price = db.Column(db.NUMERIC(10,2), nullable=False)
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)
    location = db.Column(db.ARRAY(db.String))
    delivery = db.Column(db.Boolean, nullable=False)
    pickup = db.Column(db.Boolean, nullable=False)
    ingredients = db.Column(db.ARRAY(db.String))

class Review(db.Model):
    id = db.Column(db.BIGINT, nullable=False, unique=True, primary_key=True)
    for_user = db.Column(db.String(20), nullable=False)
    by_user = db.Column(db.String(20), nullable=False)
    item = db.Column(db.String(80))
    rating = db.Column(db.Integer, nullable=False) # 1-5 stars
    review = db.Column(db.String(140))
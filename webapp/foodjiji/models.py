from foodjiji import db
import numpy

class Account(db.Model):
    username = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    account_type = db.Column(db.BOOLEAN, nullable=False)
    preference = db.Column(db.ARRAY(db.Float))

    def __init__(self, username, email, account_type):
        self.username = username
        self.email = email
        self.account_type = account_type
        self.preference = numpy.zeros(1000)


class Post(db.Model):
    id = db.Column(db.BIGINT, nullable=False, unique=True, primary_key=True)
    item = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(140))
    price = db.Column(db.NUMERIC(10,2), nullable=False)
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)
    location = db.Column(db.String)
    delivery = db.Column(db.BOOLEAN, nullable=False)
    pickup = db.Column(db.BOOLEAN, nullable=False)
    ingredients = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    
    def __init__(self, item, user, description, price, start_date, end_date, location, delivery, pickup, ingredients, image):
        self.item = item
        self.user = user
        self.description = description
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.delivery = delivery
        self.pickup = pickup
        self.ingredients = ingredients
        self.image = image

class Review(db.Model):
    id = db.Column(db.BIGINT, nullable=False, unique=True, primary_key=True)
    for_user = db.Column(db.String(20), nullable=False)
    by_user = db.Column(db.String(20), nullable=False)
    item = db.Column(db.String(80))
    rating = db.Column(db.Integer, nullable=False) # 1-5 stars
    review = db.Column(db.String(140))

    def __init__(self, for_user, by_user, item, rating, review):
        self.for_user = for_user
        self.by_user = by_user
        self.item = item
        self.rating = rating
        self.review = review
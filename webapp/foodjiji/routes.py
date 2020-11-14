from foodjiji import app
from flask import render_template
from foodjiji.models import User, Post, Review

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

@app.route("/", methods =['POST'])
def webapp():
    prediction = 1
    #return a html file
    return render_template('templates.html', prediction = prediction, posts = posts)

@app.route('/', methods=['GET'])
def load():
    return render_template('templates.html', prediction=None)
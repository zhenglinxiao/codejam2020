# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:29:55 2019

@author: liuyu
"""
#IMPORT
from flask import Flask, request, render_template

#METHODS
#Dummy data
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

#WEBAPP
app = Flask(__name__)

@app.route("/", methods =['POST'])
def webapp():
    prediction = 1
    #return a html file
    return render_template('templates.html', prediction = prediction, posts = posts)

@app.route('/', methods=['GET'])
def load():
    return render_template('templates.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)

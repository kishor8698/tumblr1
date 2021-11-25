from flask import render_template
from tumblr1 import app,db
from tumblr1.models import User,Post,Comment,Like
from tumblr1 import admin

# @app.route('/')
@app.route('/')
def home_page():
    result=User.query.all()[0]
    print(result)
    return render_template('homepage.html',result=result)
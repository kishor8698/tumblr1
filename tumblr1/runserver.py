from flask import Flask
from tumblr1 import app  
from tumblr1.models import db

# db.init_app(app)

if __name__=='__main__':
    app.run(debug=True)
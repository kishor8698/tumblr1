
# from flask_login import LoginManager, login_user, UserMixin, logout_user,current_user
import enum
from datetime import datetime
from tumblr1 import db#,login_manager
from flask_login import UserMixin

class POST_TYPE(enum.Enum):
    IMAGE='Image'
    AUDIO='Audio'
    VIDEO='Video'
    TEXT='Text'
    GIF='Gif'
    
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False,unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    #----------default none values -------------------------------
    user_image = db.Column(db.String(255),default=None)
    website_url = db.Column(db.String(255),default=None)
    facebook = db.Column(db.String(255),default=None)
    twitter = db.Column(db.String(255),default=None)
    instagram = db.Column(db.String(255),default=None)
    linkedin =db.Column(db.String(255),default=None)
    
    def __repr__(self):
        return f'User {self.user_id} : {self.username} : {self.email} : {self.password}'
    
    # @property
    # def show(self):
    #     name = self.name
    #     if name.islower():
    #         return name.upper()

class Post(db.Model): #,UserMixin): #Question
    __tablename__ = 'Post'
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(255), nullable=False)
    post_description = db.Column(db.String(255), nullable=False)
    post_data = db.Column(db.String(255), nullable=False)
    post_type= db.Column(db.Enum(POST_TYPE), nullable=False)
    post_datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id',ondelete="CASCADE"),nullable=False)
    user = db.relationship('User', backref=db.backref('post', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.post_title

class Comment(db.Model):#,UserMixin):
    __tablename__ = 'Comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(255), nullable=False)
    comment_datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id',ondelete="CASCADE"),nullable=False)
    
    # person_id = db.Column(db.Integer, db.ForeignKey('Person.person_id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comment', lazy=True))
    user = db.relationship('User', backref=db.backref('comment', lazy=True)) 

    def __repr__(self):
        return '<Comment %r>' % self.comment_text

class Like(db.Model):#,UserMixin):
    __tablename__ = 'Like'
    like_id = db.Column(db.Integer, primary_key=True)
    like_post=db.Column(db.String(255), nullable=False,default=None)
  
    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id',ondelete="CASCADE"),nullable=False)

    post = db.relationship('Post', backref=db.backref('Like', lazy=True))
    user = db.relationship('User', backref=db.backref('Like', lazy=True)) 

    def __repr__(self):
        return '<Like %r>' % self.like_id
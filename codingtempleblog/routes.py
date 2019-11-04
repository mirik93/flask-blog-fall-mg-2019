from codingtempleblog import app, db
from flask import render_template, request, flash, redirect, url_for

# import of forms
from codingtempleblog.forms import SignUpForm, LoginForm, PostForm

#import models
from codingtempleblog.models import User,check_password_hash,Post

#import flask login module/functions
from flask_login import login_user, current_user, logout_user

import stripe

# Home Route
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("home.html",posts = posts)

@app.route("/register",methods=["Get","Post"])
def createUser():
    form = SignUpForm()
    if request.method == 'POST' and  form.validate():
        flash("Thanks for Signing up!")
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username,email,password)

        #add form data to user model class
        user = User(username,email,password)
        db.session.add(user) #start comms with database
        db.session.commit() #save data to database
        return redirect(url_for('login'))

    else:
        print("Not valid")
    return render_template('register.html',register_form=form)

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user_email = form.emil.data
        password = form.password.data
        logged_user = User.query.filter(User.email == user_email).first
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    return render_template('login.html',login_form = form)

@app.route('/post',methods=["GET","POST"])
def post():
    form = PostForm()
    title = form.title.data
    content = form.content.data
    user_id = current_user.data

    #instatiate post class
    post = Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()
    return render_template('post.html',post_form = form)


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(Post.id)
    return render_template('post_detail.html',post=post)

@app.route('/payment',methods=['GET','POST'])
def payment():
    #set your secret key: remember to change this your live secret key in pro
    #see your keys here: https://dashboard.stripe.com/account/apikeys
    stripe.api_key = 'sk_test_9TeCZ25j0vTd08anOqF1kYK4'
    publishable_key = 'pk_test_eX3r0a7vvFodinoX73MqSrDN'
    price = 5000

    return render_template('payment.html',key=publishable_key,price=price)

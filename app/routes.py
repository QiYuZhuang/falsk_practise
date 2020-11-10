from flask import render_template, flash, redirect, url_for

from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm
from app.models import User

@app.route("/")
def index():
    return render_template('index.html', title='Home')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registration success', category='success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        passward = form.password.data
        flash("Success login in!")
    return render_template('login.html', form=form)
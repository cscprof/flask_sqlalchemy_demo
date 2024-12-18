'''
This file will setup the routes (URLs) for user authentication.
'''
from flask import render_template, redirect, url_for, flash

from . import users
from app.models.user import User
from app.extensions import Base, engine, session

from flask_login import current_user, login_user, logout_user
from sqlalchemy import select, insert

from .forms import LoginForm, RegistrationForm


# Route for the user listing
@users.route('/users')
def user_listing():

    Base.metadata.create_all(engine)
    results = session.query(User).all()

    return render_template('users/listing.html', users = results)


# Route for logging in
@users.route('/auth/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Create the Add Laptop Form
    form = LoginForm()

    if form.validate_on_submit():        
        
        user = session.scalar( select(User).where(User.email == form.email.data) )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        
        # login_user(user, remember=form.remember_me.data)
        login_user(user)

        url = '/users'
        return redirect(url, 302)

    return render_template('auth/login.html', form=form)

# Route for logging out
@users.route('/auth/logout')
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('main.index'))


# Route for Registration
@users.route('/auth/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('We validated!')
         
        u = User( firstname=form.firstname.data
                    , nickname=form.nickname.data
                    , lastname=form.lastname.data
                    , email=form.email.data
                    , is_Admin = False)
        
        u.set_password(form.password.data)

        session.add(u)
        session.flush()
        session.commit()
        
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('users.login'))
    
    return render_template('auth/register.html', form=form)
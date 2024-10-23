# Imports to handle form processing
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email

'''
    NOTE: This is where all WT Forms classes will be defined for this module
'''

# Form definition for adding a user to the database
class AddUserForm(FlaskForm):
    firstname = StringField('First Name:', validators=[DataRequired(message="Enter your first name"), Length(max=50)])
    lastname = StringField('Last Name:', validators=[DataRequired(message="Enter your last name"), Length(max=50)])
    
    email = EmailField('Email:', validators=[DataRequired(), Email("This field requires a valid email address")])
    password = PasswordField('Password:', validators=[DataRequired()])  

    submit = SubmitField('Add User')


class LoginForm(FlaskForm):
    email = EmailField('Email:', validators=[DataRequired(), Email("This field requires a valid email address")])
    password = PasswordField('Password:', validators=[DataRequired()])  

    submit = SubmitField('Login')
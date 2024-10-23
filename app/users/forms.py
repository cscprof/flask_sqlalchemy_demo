# Imports to handle form processing
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# Imports to handle registration
from app.extensions import session
from app.models.user import User
from sqlalchemy import select

'''
    NOTE: This is where all WT Forms classes will be defined for this module
'''

# Form definition for adding a user to the database
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name:', validators=[DataRequired(message="Enter your first name"), Length(max=64)])
    lastname = StringField('Last Name:', validators=[DataRequired(message="Enter your last name"), Length(max=64)])
    nickname = StringField('Nickame:', validators=[Length(max=64)])
    
    email = EmailField('Email:', validators=[DataRequired(), Email("This field requires a valid email address")])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Add User')

    # When you add any methods that match the pattern validate_<field_name>, WTForms takes those as 
    # custom validators and invokes them in addition to the stock validators. 
    def validate_email(self, email):
        user = session.scalar(select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Email address already in use.  Choose another.')




class LoginForm(FlaskForm):
    email = EmailField('Email:', validators=[DataRequired(), Email("This field requires a valid email address")])
    password = PasswordField('Password:', validators=[DataRequired()])  

    submit = SubmitField('Login')


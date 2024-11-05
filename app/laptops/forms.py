# Imports to handle form processing
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField, RadioField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange

'''
    NOTE: This is where all WT Forms classes will be defined for this module
'''

# Form definition for adding a laptop to the database
class AddLaptopForm(FlaskForm):
    brand = StringField('Brand:', validators=[DataRequired(message="Enter a brand (e.g. Dell, Apple)"), Length(max=50)])
    
    model = StringField('Model:', validators=[Length(max=255) ])
    
    price = DecimalField('Price:', validators=[DataRequired(message="Enter the purchase price.")
                , NumberRange(min=0.01,  message="Price must be greater than $0")])
    
    ram_memory = IntegerField('RAM (GB):', validators=[DataRequired(message="Amount of RAM is required")
                , NumberRange(min=2, max=128, message="Enter memory amount between 2 and 128")])
    
    rating = IntegerField('Ratung:', validators=[DataRequired(message="Rating on scale of 1 to 100")
                , NumberRange(min=2, max=128, message="Enter memory amount between 1 and 100")])
    touch_screen = RadioField('Touch Screen:', choices=[ (0,"No"), (1,"Yes") ], validators=[DataRequired()])
    processor_id = SelectField('Processor:', validators=[DataRequired()])
    submit = SubmitField('Add Laptop')
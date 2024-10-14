from flask import Flask, render_template, redirect
import mariadb
import myDatabase as db
import sys
from sql_queries import vehicle_query as vc
from sql_queries import vendor_query
from sql_queries import laptop_query

# Include the configuration class
from config import Config

# Imports to handle form processing
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

# Define a Constant
UPDATE_EXCEPTION = -1
DUPLICATE_VENDOR = -2

# Launch app and define where the static assets will be located
app = Flask(__name__, static_url_path='/static')

# Need a secret key for security (CSRF protection)
app.secret_key = Config.SECRET_KEY

"""

    ******** Vehicles Section ********

"""


@app.route('/')
def available():
     # Connect to MariaDB Platform
    try:
        conn=db.myConnect()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor(dictionary=True)

    # Execute Query
    cur.execute(vc.sellable_vehicles)

    output = cur.fetchall()

    # Return to the browser - View template = listing.html with in-template variable = vehicles
    return render_template('vehicles/listing.html', vehicles=output, forsale=True)


@app.route('/vehicles')
def all_vehicles():

    # Connect to MariaDB Platform
    try:
        conn=db.myConnect()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor(dictionary=True)

    # Execute Query
    cur.execute( vc.all_vehicles)
    output = cur.fetchall()

    # Return to the browser - View template = listing.html with in-template variable = vehicles
    return render_template('vehicles/listing.html', vehicles=output, forsale=False)


"""

    ******** Vendors Section ********

"""

'''
WT Forms implementation of the Add Vendor Form.
'''
class AddVendorForm(FlaskForm):
    vendor_name = StringField('Vendor Name:', validators=[DataRequired()])
    phone_number = StringField('Phone:', validators=[DataRequired()])
    street = StringField('Street:', validators=[DataRequired()])
    city = StringField('City:', validators=[DataRequired()])
    state = StringField('State:', validators=[DataRequired()])
    postal_code = StringField('Postal Code:', validators=[DataRequired()])
    submit = SubmitField('Add Vendor')


@app.route('/vendors')
def vendors():

    vc = vendor_query.Vendors()

    # Connect to MariaDB Platform
    try:
        conn=db.myConnect()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor(dictionary=True)

    # Execute Query
    cur.execute( vc.vendor_list() )
    output = cur.fetchall()

    # Return to the browser - View template = listing.html with in-template variable = vendors
    return render_template('vendors/listing.html', vendors=output)

@app.route('/vendors/add', methods=['GET', 'POST'])
def vendor_add():

    # Get instance of query class
    vc = vendor_query.Vendors()

    # Get instance of add form class
    form = AddVendorForm()

    if form.validate_on_submit():
        data = {}
        data['vendor_name'] = form.vendor_name.data
        data['phone_number'] = form.phone_number.data
        data['street'] = form.street.data
        data['city'] = form.city.data
        data['state'] = form.state.data
        data['postal_Code'] = form.postal_code.data

        sql = vc.add_vendor(data)

        # Connect to MariaDB Platform
        try:
            conn=db.myConnect()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor(dictionary=True)

        try:
            # Attempt to save the vendor
            cur.execute(sql)
            id = cur.lastrowid
            conn.commit()

        except conn.IntegrityError as err:
            # Catch the integrity violation here
            print(err.errno)
            print(err.sqlstate)
            print(err.msg)

            id = -2
        except:
            # Catch stray exceptions
            print(err.errno)
            print(err.sqlstate)
            print(err.msg)
            id = -1


        if id == DUPLICATE_VENDOR:
            # Tried to crate a duplicate vendor
            form = AddVendorForm(formdata=None)
            return render_template('vendors/addvendor.html', form=form)
        else:
            # Vendor was created
            url = '/vendors'
            return redirect(url, 302)

    return render_template('vendors/addvendor.html', form=form)


"""

    ******** Laptops Section ********

"""
class AddLaptopForm(FlaskForm):

    brand = StringField('Brand:', validators=[DataRequired(message="Enter a brand (e.g. Dell, Apple)"), Length(max=50)])
    model = StringField('Model:', validators=[Length(max=255) ])
    price = DecimalField('Price:', validators=[DataRequired(message="Enter the purchase price.")
                , NumberRange(min=0.01,  message="Price must be greater than $0")])
    ram_memory = IntegerField('RAM (GB):', validators=[DataRequired(message="Amount of RAM is required")
                , NumberRange(min=2, max=128, message="Enter memory amount between 2 and 128")])
    rating = IntegerField('Rating:', validators=[DataRequired(message="Rating on scale of 1 to 100")
                , NumberRange(min=0, max=100, message="Enter memory amount between 0 and 100")])
    touch_screen = RadioField('Touch Screen:', choices=[ (0,"No"), (1,"Yes") ], validators=[DataRequired()])
    processor_id = SelectField('Processor:', validators=[DataRequired()])
    submit = SubmitField('Add Laptop')

#
#   Laptop Listing Page
#
@app.route('/laptops')
def laptops():

    vc = laptop_query.Laptops()

    # Connect to MariaDB Platform
    try:
        conn=db.myConnect()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor(dictionary=True)

    # Execute Query
    cur.execute( vc.laptop_list() )
    output = cur.fetchall()

    # Return to the browser - View template = listing.html with in-template variable = laptops
    return render_template('/laptops/listing.html', laptops=output)

#
#   Add Laptop Page
#
@app.route('/laptops/add', methods=['GET', 'POST'])
def laptop_add():

    # Get instance of query class
    vc = laptop_query.Laptops()

    # Get list of processors
    choices = build_processor_list()

    # Get instance of add form class
    form = AddLaptopForm()
    form.processor_id.choices = choices

    if form.validate_on_submit():
        data = {}

        data['model'] = form.model.data
        data['processor_id'] = form.processor_id.data
        data['ram_memory'] = form.ram_memory.data
        data['touch_screen'] = form.touch_screen.data
        data['rating'] = form.rating.data
        data['brand'] = form.brand.data
        data['price'] = form.price.data

        sql = vc.add_laptop(data)

        print(data)

        # Connect to MariaDB Platform
        try:
            conn=db.myConnect()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor(dictionary=True)

        try:
            # Attempt to save the laptop
            cur.execute(sql)
            id = cur.lastrowid
            conn.commit()

        except mariadb.Error as err:
            # Catch stray exceptions
            print(err.errno)
            print(err.sqlstate)
            print(err.msg)
            id = UPDATE_EXCEPTION

        if id == UPDATE_EXCEPTION:
            # Failed adding a laptop
            form = AddLaptopForm(formdata=None)
            return render_template('/laptops/addlaptop.html', form=form)
        else:
            # Vendor was created
            url = '/laptops'
            return redirect(url, 302)

    return render_template('/laptops/addlaptop.html', form=form)



def build_processor_list():

    # Get instance of query class
    vc = laptop_query.Laptops()

    try:
        conn=db.myConnect()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor(dictionary=True)

    # Execute Query
    cur.execute( vc.processor_list() )
    output = cur.fetchall()

    choices = []

    # Create list of tuples (id, processor type)
    for item in output:
        choices.append( (item['processor_id'], item['processor']) )

    return choices




'''
Easy launch of application

    If this ile is being executed, __name__ will be equal to __main__ and the code below it will run.

    More info can be found here: https://medium.com/@mycodingmantras/what-does-if-name-main-mean-in-python-fa6b0460a62d
    Scripts vs modules
'''
if __name__ == "__main__":
    app.run(debug=True)
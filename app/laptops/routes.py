'''
This file will setup the routes (URLs) for each of the reports.
The actual report code will be in classes in separate files.
'''
from flask import render_template, session, redirect, url_for, flash
# from app.extensions import db
# from sqlalchemy.orm import Session

from . import laptops
from app.models.laptop import Laptop

from . import AddLaptop
from .forms import AddLaptopForm


# Route for the laptop listing
@laptops.route('/laptops')
def laptop_listing():
    listing = Laptop.query.all()    
    return render_template('listing.html', laptops = listing)


# Route for adding a laptop to the database
@laptops.route('/laptops/add', methods=['GET', 'POST'])
def laptopAdd():

    # Get list of processors
    al = AddLaptop.AddLaptop()
    processors = al.buildProcessorList()

    # Create the Add Laptop Form
    form = AddLaptopForm()
    form.processor_id.choices = processors

    if form.validate_on_submit():

        print('We are adding a laptop here!!!!!')
        
        id = al.laptop_add(form)
        print(f'New id: {id}')
        
        url = '/laptops'
        return redirect(url, 302)

    return render_template('addlaptop.html', form=form)



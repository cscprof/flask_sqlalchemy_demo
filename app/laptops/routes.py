'''
This file will setup the routes (URLs) for each of the reports.
The actual report code will be in classes in separate files.
'''
from flask import render_template, redirect, url_for, flash

from . import laptops
from app.models.laptop import Laptop
from app.extensions import Base, engine, session


from . import AddLaptop
from .forms import AddLaptopForm


# Route for the laptop listing
@laptops.route('/laptops')
def laptop_listing():

    Base.metadata.create_all(engine)

    results = session.query(Laptop).all()
    # for laptop in results:
    #     print(f"ID: {laptop.processor.processor_id} Model: {laptop.processor.processor_name}")

    return render_template('laptops/listing.html', laptops = results)


# Route for adding a laptop to the database
@laptops.route('/laptops/add', methods=['GET', 'POST'])
def laptopAdd():

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

    return render_template('laptops/addlaptop.html', form=form)



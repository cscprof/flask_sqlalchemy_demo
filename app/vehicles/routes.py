'''
This file will setup the routes (URLs) for each of the reports.
The actual report code will be in classes in separate files.
'''
from flask import render_template, session, redirect, url_for, flash
# from app.extensions import db
# from sqlalchemy.orm import Session

from . import vehicles

# from app.models.vehicle import Vehicle
# from app.models.color import Color

from app.models.vehicle_color import Vehicle
from app.models.vehicle_color import Color


# Route for the laptop listing
@vehicles.route('/vehicles')
def vehicle_listing():
    listing = Vehicle.query.all()   
    # print(listing) 
    return render_template('listing2.html', vehicles = listing)

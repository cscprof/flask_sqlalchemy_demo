'''
This file will setup the routes (URLs) for each of the reports.
The actual report code will be in classes in separate files.
'''
from flask import render_template, session, redirect, url_for, flash
# from app.extensions import db
# from sqlalchemy.orm import Session

from . import vehicles

from app.models.vehicle import Vehicle

from app.models.vehicletype import VehicleType
from app.extensions import Base, engine, session
# from app.models.vehicle_color import Color


# Route for the vehicles listing
@vehicles.route('/vehicles')
def vehicle_listing():

    Base.metadata.create_all(engine)

    results = session.query(Vehicle).all()

    # for vehicle in results:
    #     c = [color.color_name for color in vehicle.colors]

    return render_template('listing2.html', vehicles = results)
    

# Route for the vehicle types listing
@vehicles.route('/vtypes')
def vehicle_types():

    Base.metadata.create_all(engine)

    results = session.query(VehicleType).all()
    for vtype in results:
        print(f"ID: {vtype.vehicle_typeID} Vehicle Type: {vtype.vehicle_type_name}")
    
    return "Got it" # render_template('listing2.html', vehicles = listing)

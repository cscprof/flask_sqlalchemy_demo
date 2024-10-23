'''
This file will setup the routes (URLs) for each of the reports.
The actual report code will be in classes in separate files.
'''
from flask import render_template, session, redirect, url_for, flash
from app.extensions import Base, engine, session

from . import vehicles
from app.models.vehicle import Vehicle
from app.models.vehicletype import VehicleType
from app.models.manufacturer import Manufacturer

from sqlalchemy import or_

# Route for the vehicles listing
@vehicles.route('/vehicles')
def vehicle_listing():

    Base.metadata.create_all(engine)
    results = session.query(Vehicle)
    # for vehicle in results:
    #     c = [color.color_name for color in vehicle.colors]

    return render_template('vehicles/listing.html', vehicles = results)
    

# Route for the vehicle types listing
@vehicles.route('/vtypes')
def vehicle_types():

    Base.metadata.create_all(engine)
    results = ( session.query(VehicleType).order_by(VehicleType.vehicle_type_name.desc())
    )
    
    return render_template('vehicles/vehicle_types.html', vehicle_types = results)

 # Route for the filtered vehicles listing
@vehicles.route('/vehicles/hybrid')
def vehicle_fueltype():

    Base.metadata.create_all(engine)
    results = ( session.query(Vehicle)
                    .join(Manufacturer)
                    .filter( Vehicle.fuel_type == "Plugin Hybrid" )
                    .order_by(Manufacturer.manufacturer_name.desc())
    )

    return render_template('vehicles/listing.html', vehicles = results)

# Route for the filtered vehicles listing
@vehicles.route('/vehicles/mfg')
def vehicle_mfg():

    mfg_list = ['Honda', 'Toyota', 'Ferrari']    

    Base.metadata.create_all(engine)
    
    # Note the ( ) surrounding session().....  Allows for prettier indentations 
    # of the session.query command string
    results = ( session.query(Vehicle)
                    .join(Manufacturer)
                    .filter( Manufacturer.manufacturer_name.in_(mfg_list) ) 
    )

    return render_template('vehicles/listing.html', vehicles = results)
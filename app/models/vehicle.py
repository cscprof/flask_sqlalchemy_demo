from app.extensions import Base

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship


class Vehicle(Base):

  # Set this to the name of the table in the database if 
  # different from the class name defined above.
  __tablename__ = "vehicles"

  # Schema definition
  vehicleID = Column(Integer, primary_key=True)
  vin = Column(String(50))
  mileage = Column(DECIMAL)
  description = Column(String(255))
  model_name = Column(String(255))
  model_year = Column(Integer)
  fuel_type = Column(String(50))

  # Vehicle Type
  vehicle_typeID = Column(Integer, ForeignKey('vehicletypes.vehicle_typeID'))
  vehicle_type = relationship('VehicleType')      

  # Manufacturer
  manufacturerID = Column(Integer, ForeignKey('manufacturers.manufacturerID'))
  manufacturer = relationship('Manufacturer')

  # Many-to-many with colors
  colors = relationship('Color', secondary='vehiclecolors', back_populates='vehicles')

  
  def __repr__(self):
      return f'<VIN: "{self.vin} Model: {self.model_name}">'
    

'''

CREATE TABLE `vehicles` (
  `vehicleID` int NOT NULL AUTO_INCREMENT,
  `vin` varchar(50) NOT NULL,
  `mileage` decimal(10,1) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `model_name` varchar(255) NOT NULL,
  `model_year` int NOT NULL,
  `fuel_type` enum('Gas','Diesel','Natural Gas','Hybrid','Plugin Hybrid','Battery','Fuel Cell') NOT NULL,
  `manufacturerID` int NOT NULL,
  `vehicle_typeID` int NOT NULL,
  PRIMARY KEY (`vehicleID`),
  UNIQUE KEY `vin` (`vin`),
  KEY `fk_Vehicles_manufacturerID_Manufacturers_manufacturerID` (`manufacturerID`),
  KEY `fk_Vehicles_vehicle_typeID_VehicleTypes_vehicle_typeID` (`vehicle_typeID`),
  CONSTRAINT `fk_Vehicles_manufacturerID_Manufacturers_manufacturerID` FOREIGN KEY (`manufacturerID`) REFERENCES `manufacturers` (`manufacturerID`),
  CONSTRAINT `fk_Vehicles_vehicle_typeID_VehicleTypes_vehicle_typeID` FOREIGN KEY (`vehicle_typeID`) REFERENCES `vehicletypes` (`vehicle_typeID`)
) ENGINE=InnoDB AUTO_INCREMENT=302 DEFAULT CHARSET=latin1;

'''
from typing import Optional, List
from sqlalchemy import String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Import Database connection
from app.extensions import db

from app.models.vehicle_color import VehicleColor



class Vehicle(db.Model):

  # Set this to the name of the table in the database if 
  # different from the class name defined above.
  __tablename__ = "vehicles"

  # Schema definition
  vehicleID : Mapped[int] = mapped_column(primary_key=True)
  vin : Mapped[str] = mapped_column(String(50))
  mileage : Mapped[DECIMAL] = mapped_column(DECIMAL)
  description : Mapped[str] = mapped_column(String(255))
  model_name : Mapped[str] = mapped_column(String(255))
  model_year : Mapped[int] = mapped_column(Integer)

  vehicle_typeID : Mapped[int] = mapped_column(ForeignKey("vehicletypes.vehicle_typeID"))
  vehicle_type: Mapped["VehicleType"] = relationship()      

  manufacturerID : Mapped[int] = mapped_column(ForeignKey("manufacturers.manufacturerID"))
  manufacturer: Mapped["Manufacturer"] = relationship()

  # Many-to-many with colors
  colors : Mapped[List["Color"]] = relationship(secondary=VehicleColor)
                                               # , back_populates="vehicles")


  
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
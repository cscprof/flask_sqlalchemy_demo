from app.extensions import Base

from sqlalchemy import Column, ForeignKey, Integer


class VehicleColor(Base):
    __tablename__ = 'vehiclecolors'
    vehicle_colorID = Column(Integer, primary_key=True )
    vehicleID = Column('vehicleID', Integer, ForeignKey('vehicles.vehicleID'))
    colorID = Column('colorID', Integer, ForeignKey('colors.colorID'))
    

'''

TABLE `vehiclecolors` (
  `vehicle_colorID` int NOT NULL AUTO_INCREMENT,
  `vehicleID` int NOT NULL,
  `colorID` int NOT NULL,
  PRIMARY KEY (`vehicle_colorID`),
  UNIQUE KEY `UC_VehicleColor` (`vehicleID`,`colorID`),
  KEY `fk_VehicleColors_colorID_Colors_colorID` (`colorID`),
  CONSTRAINT `fk_VehicleColors_colorID_Colors_colorID` FOREIGN KEY (`colorID`) REFERENCES `colors` (`colorID`),
  CONSTRAINT `fk_VehicleColors_vehicleID_Vehicles_vehicleID` FOREIGN KEY (`vehicleID`) REFERENCES `vehicles` (`vehicleID`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=latin1;

'''
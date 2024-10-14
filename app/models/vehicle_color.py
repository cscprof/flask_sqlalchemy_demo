from typing import List
from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


# New stuff here
from sqlalchemy import Table, Column, String, Integer, DECIMAL
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


VehicleColor = Table(
    "vehiclecolors",
    Base.metadata,
    Column("vehicle_colorID", primary_key=True ),
    Column("colorID",   ForeignKey("colors.colorID")),
    Column("vehicleID", ForeignKey("vehicles.vehicleID"))
)


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
  # colors : Mapped[List["Color"]] = relationship(secondary=VehicleColor,
  #                                               primaryjoin="vehicles.vehicleID == vehiclecolors.vehicleID",
  #                                               secondaryjoin= "vehiclecolors.colorID == colors.colorID")
      
                                                # secondary=VehicleColor)
                                               # , back_populates="vehicles")


class Color(db.Model):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "colors"

    # Schema definition
    colorID :  Mapped[int] = mapped_column(primary_key=True)
    color_name : Mapped[str] = mapped_column(String(50))

    # Many-to-many with vehicles
    # vehicles : Mapped[List["Vehicle"]] = relationship(secondary=VehicleColor)
    #                                                 #,back_populates="colors")
  

    def __repr__(self):
        return f'<Color ID: {self.colorID} - {self.color_name}>'
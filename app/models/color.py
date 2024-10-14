from typing import Optional, List
from sqlalchemy import String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db

from app.models.vehicle_color import VehicleColor

class Color(db.Model):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "colors"

    # Schema definition
    colorID :  Mapped[int] = mapped_column(primary_key=True)
    color_name : Mapped[str] = mapped_column(String(50))

    # Many-to-many with vehicles
    vehicles : Mapped[List["Vehicle"]] = relationship(secondary=VehicleColor)
                                                    #,back_populates="colors")
  

    def __repr__(self):
        return f'<Color ID: {self.colorID} - {self.color_name}>'
    

'''

CREATE TABLE `colors` (
  `colorID` int NOT NULL AUTO_INCREMENT,
  `color_name` varchar(50) NOT NULL,
  PRIMARY KEY (`colorID`),
  UNIQUE KEY `color_name` (`color_name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

'''
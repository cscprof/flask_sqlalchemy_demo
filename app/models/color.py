from app.extensions import Base

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

# from app.models.vehicle import Vehicle

class Color(Base):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "colors"

    # Schema definition
    colorID = Column(Integer, primary_key=True)
    color_name = Column(String(50))

    # Many-to-many with vehicles
    vehicles = relationship('Vehicle', secondary='vehiclecolors', back_populates='colors')
                                                   
    def __repr__(self):        
        return f'{self.color_name}'
    

'''

CREATE TABLE `colors` (
  `colorID` int NOT NULL AUTO_INCREMENT,
  `color_name` varchar(50) NOT NULL,
  PRIMARY KEY (`colorID`),
  UNIQUE KEY `color_name` (`color_name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

'''
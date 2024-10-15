from app.extensions import engine, session, Base

from sqlalchemy import Column, Integer, String

class VehicleType(Base):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "vehicletypes"

    # Schema definition
    vehicle_typeID = Column(Integer, primary_key=True)    
    vehicle_type_name = Column(String(50))
    
    
    def __repr__(self):
        return f'<Vehicle Type ID: {self.vehicle_typeID} - {self.vehicle_type_name}>'
    

'''

CREATE TABLE `vehicletypes` (
  `vehicle_typeID` int NOT NULL AUTO_INCREMENT,
  `vehicle_type_name` varchar(50) NOT NULL,
  PRIMARY KEY (`vehicle_typeID`),
  UNIQUE KEY `vehicle_type_name` (`vehicle_type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

'''